from Producto import Producto
from Orden import Orden

producto1 = Producto('papas', 25)
producto2 = Producto('chicharrones', 50)
producto3 = Producto('refrresco', 75)
producto4 = Producto('botas', 15)

orden1 = Orden([producto1, producto2])
orden2 = Orden([producto3, producto4])

orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

print(orden1)
print(f'total de la orden: {orden1.calcular_total()}')
