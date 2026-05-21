from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, utasok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__utasok_szama = utasok_szama

    @property
    def utasok_szama(self):
        return self.__utasok_szama

    def informacio(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, Utasok: {self.__utasok_szama}"