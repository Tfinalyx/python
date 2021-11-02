from cuadrado import Cuadrado
from rectangulo import Rectangulo
print(f'Creacion de objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1)
print(f'el area es:{cuadrado1.area()}')

print(f'Creacion de objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(0, 6, 'verde')
print(rectangulo1)
print(f'el area es:{rectangulo1.area()}')
#print(Cuadrado.mro())

