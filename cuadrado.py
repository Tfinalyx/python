from figuraGeometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        self._lado = lado
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # @property  # get color
    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'propiedades: {FiguraGeometrica.__str__(self)},{Color.__str__(self)}'
