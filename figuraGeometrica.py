from abc import ABC,abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        if alto > 0 and ancho > 0:
            self._alto = alto
            self._ancho = ancho
        else:
            self._alto = 0
            self._ancho = 0

    @property  # get color
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property  # get color
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'alto:{self._alto}, ancho:{self._ancho}'
