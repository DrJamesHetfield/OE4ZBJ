from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self.__teherbiras

    def informacio(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, Teherbírás: {self.__teherbiras} kg"