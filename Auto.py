from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berleti_dij = berleti_dij

    #getterek a non-public attributumokhoz
    @property
    def rendszam(self):
        return self.__rendszam

    @property
    def tipus(self):
        return self.__tipus

    @property
    def berleti_dij(self):
        return self.__berleti_dij

    #absztrakt metódus definiálása
    @abstractmethod
    def informacio(self):
        pass