import matplotlib.pyplot as plt

from passeggiata_aleatoria import PasseggiataAleatoria

#creare l'oggetto Passeggiata aleatoria

pa = PasseggiataAleatoria()
#print(f"primi passi x:{pa.x}, y: {pa.y}")

pa.fare_passeggiata()
#print(f"passi finali x: {pa.x}, y: {pa.y}")

plt.style.use("dark_background")
fig, ax = plt.subplots() # figura, asse (variabili chiamate da noi)
ax.scatter(pa.x, pa.y, s=20, c=pa.x, cmap=plt.cm.plasma)

plt.show()