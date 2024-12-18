import matplotlib.pyplot as plt

massimo_input = 1000
input_valori = range(1, massimo_input + 1)
quadrati = [x ** 2 for x in input_valori]

# plt.style.available per vedere gli stili disponibili
plt.style.use("dark_background")
fig, ax = plt.subplots() # figura, asse (variabili chiamate da noi)
ax.scatter(input_valori, quadrati, s=2000, c=quadrati, cmap=plt.cm.plasma) # = x, y; s è la dimensione del pallino, plasma = temperatura da fredda a calda
# scatter non collega i puntini
ax.set_title("Quadrati dei numeri", fontsize=24)
ax.set_xlabel("Valore", fontsize=14)
ax.set_ylabel("Quadrati", fontsize=14)
ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1_100_000]) # estremi degli assi x e y, l'underscore aiuta a spaziare le migliaia
ax.ticklabel_format(style="plain")

counter = 3
plt.savefig(f"img/figura_quadrati{counter}.png", bbox_inches="tight") #tight lascia poco spazio bianco ai lati
plt.show()