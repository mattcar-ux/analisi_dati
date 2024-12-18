from pathlib import Path
import json
import plotly.express as px

percorso = Path("tm_dati\\tm_1_giorno.geojson") # percorso relativo, oggetto path (meglio la doppia barra)
contenuti = percorso.read_text(encoding="utf-8")
tutti_tm = json.loads(contenuti) # carica i contenuti dal file geojson

# per creare una copia più leggibile
# percorso = Path("tm_dati\\leggibile_tm_1_giorno.geojson")
# contenuti_leggibili = json.dumps(tutti_tm, indent=4) # scarica questi dati con questa indentazione
# percorso.write_text(contenuti_leggibili)

tutti_tm_dicts = tutti_tm["features"]

mags, longitudini, latitudini = [], [], []
for tm_dict in tutti_tm_dicts:
    mag = tm_dict["properties"]["mag"]
    if mag < 0: # escludo magnitudo negative
        # mag = 0
        continue # salta l'indice se magnitudo negativa
    mags.append(mag)
    lon = tm_dict["geometry"]["coordinates"][0]
    lat = tm_dict["geometry"]["coordinates"][1]
    longitudini.append(lon)
    latitudini.append(lat)

titolo = "Terremoti mondiali di oggi"
fig = px.scatter_geo(lat=latitudini, lon=longitudini, size=mags, title=titolo)
fig.show()