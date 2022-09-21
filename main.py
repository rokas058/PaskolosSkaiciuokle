import pandas as pd


pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)


class Paskola:
    def __init__(self, suma, palukanos, terminas):
        self.suma = suma
        self.palukanos = palukanos
        self.terminas = terminas

    def paskolos_info(self):
        palukanos = self.priskaiciuotos_palukanos()
        bendra_suma = self.bendra_suma()
        return f'jusu suma: {self.suma}, palukanos: {self.palukanos}%, terminas: {self.terminas} menesiu, moketinos ' \
               f'palukanos: {round(palukanos[-1], 2)}, bendra suma: {bendra_suma[-1]}'

    def menesio_nr(self):
        terminas = self.terminas
        listas = []
        while True:
            termino_nr = terminas - 1
            if termino_nr == 0:
                listas.append(self.terminas)
                break
            else:
                listas.append(termino_nr)
                terminas = termino_nr
        listas.sort()
        listas.reverse()
        listas.append('Total')
        return listas

    def grazintina_dalis(self):
        grazinta_dalis = self.suma / self.terminas
        listas = []
        for x in range(self.terminas):
            listas.append(grazinta_dalis)
        listas.append(self.suma)
        return listas

    def likutis(self):
        suma = self.suma
        listas = []
        for x in range(self.terminas):
            listas.append(suma)
            suma -= (self.suma / self.terminas)
        listas.append(0)
        return listas

    def priskaiciuotos_palukanos(self):
        likutis = self.likutis()
        listas = []
        suma = 0
        for x in likutis:
            if x == 0:
                break
            else:
                a = x / 100 * self.palukanos / 12
                b = round(a, 2)
                listas.append(b)
                suma += b
        listas.append(suma)
        return listas

    def bendra_suma(self):
        likutis = self.suma / self.terminas
        listas = []
        priskaiciuota = 0
        palukanos = self.priskaiciuotos_palukanos()
        for x in palukanos:
            if x == palukanos[-1]:
                break
            else:
                bendra = x + likutis
                listas.append(bendra)
                priskaiciuota += bendra
        listas.append(priskaiciuota)
        return listas

    def mokejimo_grafikas(self):
        menesio_nr = self.menesio_nr()
        grazinta_dalis = self.grazintina_dalis()
        likutis = self.likutis()
        priskaiciuotos_palukanos = self.priskaiciuotos_palukanos()
        bendra_suma = self.bendra_suma()

        grafikas = {'Mėn.Nr.': menesio_nr, 'Grąžintina dalis, Eur': grazinta_dalis, 'Likutis, Eur': likutis,
                    'Priskaičiuotos ''palūkanos, Eur': priskaiciuotos_palukanos,
                    'Bendra Mokėtina suma, Eur': bendra_suma}
        data = pd.DataFrame(grafikas)
        data1 = data.set_index('Mėn.Nr.')
        return data1










