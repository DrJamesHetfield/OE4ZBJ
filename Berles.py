from Auto import Auto
from datetime import date

class Berles:
    def __init__(self, auto: Auto, datum: date):
        self.__auto = auto
        self.__datum = datum

    @property
    def auto(self):
        return self.__auto

    @property
    def datum(self):
        return self.__datum