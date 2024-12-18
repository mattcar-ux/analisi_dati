from pathlib import Path
import json
import plotly.express as px
from datetime import datetime

percorso = Path("tm_dati\\all_month.geojson") # percorso relativo, oggetto path (meglio la doppia barra)
contenuti = percorso.read_text(encoding="utf-8")
tutti_tm = json.loads(contenuti) # carica i contenuti dal file geojson

# per creare una copia più leggibile
# percorso = Path("tm_dati\\leggibile_tm_1_giorno.geojson")
# contenuti_leggibili = json.dumps(tutti_tm, indent=4) # scarica questi dati con questa indentazione
# percorso.write_text(contenuti_leggibili)

tutti_tm_dicts = tutti_tm["features"]

mags, longitudini, latitudini, tm_titoli = [], [], [], []
for tm_dict in tutti_tm_dicts:
    mag = tm_dict["properties"]["mag"]
    if mag == None:
        continue # salta l'indice se magnitudo negativa
    elif mag < 0: # escludo magnitudo negative
        mag = 0
    mags.append(mag)
    lon = tm_dict["geometry"]["coordinates"][0]
    lat = tm_dict["geometry"]["coordinates"][1]
    longitudini.append(lon)
    latitudini.append(lat)
    titolo = tm_dict["properties"]["title"]
    tm_titoli.append(titolo)

time_generated = str(tutti_tm["metadata"]["generated"])
time_generated = time_generated[:-3]
dt = datetime.fromtimestamp(int(time_generated))
titolo_figura = tutti_tm["metadata"]["title"]
fig = px.scatter_geo(lat=latitudini, lon=longitudini, size=mags,
                     title=f"{titolo_figura}, generated on {dt}",
                     color=mags,
                     color_continuous_scale="electric",
                     labels={"color": "Magnitudo"},
                     projection="natural earth",
                     hover_name=tm_titoli)
fig.show()