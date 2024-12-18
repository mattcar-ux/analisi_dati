import matplotlib.pyplot as plt

quadrati = [1, 4, 9, 16, 25]
input_valori = [1, 2, 3, 4, 5]

# plt.style.available per vedere gli stili disponibili
plt.style.use('fast')
fig, ax = plt.subplots() # figura, asse (variabili chiamate da noi)
ax.plot(input_valori, quadrati, linewidth=3)

#Impostare titoli del grafico e assi
ax.set_title("Quadrati dei numeri", fontsize=24)
ax.set_xlabel("Valore", fontsize=14)
ax.set_ylabel("Quadrati", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()