from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from FtoC import converti_temperatura

percorso = Path("dati_meteo\\sitka_weather_2021_simple.csv") # percorso relativo, oggetto path (meglio la doppia barra)
righe = percorso.read_text(encoding="utf-8").splitlines()

reader = csv.reader(righe)
prima_riga = next(reader)

# for indice, contenuti in enumerate(prima_riga):
#     print(indice, contenuti)

temp_basse, temp_alte, temp_date = [], [], []
for riga in reader:
    temp_alta = converti_temperatura(int(riga[4]))
    temp_alte.append(temp_alta)
    temp_data = datetime.strptime(riga[2], "%Y-%m-%d")
    temp_date.append(temp_data)
    temp_bassa = converti_temperatura(int(riga[5]))
    temp_basse.append(temp_bassa)

# plt.style.available per vedere gli stili disponibili
#plt.style.use("dark_background")
fig, ax = plt.subplots() # figura, asse (variabili chiamate da noi)
ax.plot(temp_date, temp_alte, color="red", alpha=0.7)
ax.plot(temp_date, temp_basse, color="blue", alpha=0.7)
ax.fill_between(temp_date, temp_alte, temp_basse, facecolor="purple", alpha=0.2) # colora lo spazio tra i due plot, alpha sfoca il colore 

#Impostare titoli del grafico e assi
ax.set_title("Tempeature alte di Sitka, Alaska, luglio 2021", fontsize=24)
ax.set_xlabel("Data", fontsize=14)
ax.set_ylabel("Temperatura", fontsize=14)
ax.tick_params(labelsize=14)
fig.autofmt_xdate() # cambia orientamento date in diagonale

plt.show()