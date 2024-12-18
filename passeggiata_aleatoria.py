from random import choice

class PasseggiataAleatoria:
    """Una classe che genera le passeggiate"""

    def __init__(self, passi=5000): #iniziatore
        self.punti = passi
        
        self.x = [0]
        self.y = [0]

    def fare_passeggiata(self):
        """calcolare tutti i punti durante la passeggiata aleatoria"""

        while len(self.x) < self.punti:

            x_direzione = choice([-1, 1])
            x_distanza = choice([0, 1, 2, 3, 4])
            x_passo = x_direzione * x_distanza
            
            y_direzione = choice([-1, 1])
            y_distanza = choice([0, 1, 2, 3, 4])
            y_passo = y_direzione * y_distanza

            #Movimenti di [0.0] non sono accettati
            if x_passo == 0 and y_passo == 0:
                continue

            x_attuale = self.x[-1] + x_passo
            y_attuale = self.y[-1] + y_passo

            self.x.append(x_attuale)
            self.y.append(y_attuale)
