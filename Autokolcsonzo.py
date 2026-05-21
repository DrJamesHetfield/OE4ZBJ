from Berles import Berles
from datetime import datetime, date

class Autokolcsonzo:
    def __init__(self, nev: str):
        self.__nev = nev
        self.__autok = []
        self.__berlesek = []

    @property
    def nev(self):
        return self.__nev

    @property
    def autok(self):
        return self.__autok

    @property
    def berlesek(self):
        return self.__berlesek

    def auto_hozzaadasa(self, auto):
        self.__autok.append(auto)

    def autoberles(self, rendszam: str, datum_str: str):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Érvénytelen dátum formátum! Helyes: ÉÉÉÉ-HH-NN")

        if datum < date.today():
            raise ValueError("Múltbeli dátumra nem lehet autót bérelni!")

        Keresett_auto = next((a for a in self.__autok if a.rendszam == rendszam), None)
        if not Keresett_auto:
            raise ValueError("Nem található ilyen rendszámú autó a rendszerben!")

        for berles in self.__berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                raise ValueError("Az autó ezen a napon már ki van bérelve!")

        uj_berles = Berles(Keresett_auto, datum)
        self.__berlesek.append(uj_berles)
        return Keresett_auto.berleti_dij

    def berles_lemondasa(self, rendszam: str, datum_str: str):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Érvénytelen dátum formátum! Helyes: ÉÉÉÉ-HH-NN")

        for berles in self.__berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.__berlesek.remove(berles)
                return True
                
        raise ValueError("Nem található ilyen bérlés a rendszerben, amit le lehetne mondani!")