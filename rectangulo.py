from figuraGeometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura,color):
        self._base = base
        self._altura = altura
        FiguraGeometrica.__init__(self, altura, base)
        Color.__init__(self, color)

    def area(self):
        return self._base * self._altura

    def __str__(self):
        return f'propiedades: {FiguraGeometrica.__str__(self)},{Color.__str__(self)}'

