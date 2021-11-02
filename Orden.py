from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        self._id_orden = Orden.incrementar_valor()
        self._productos = list(productos)

    @classmethod
    def incrementar_valor(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total


    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|' + '\n'

        return f'Orden numero: [{self._id_orden}], \n{productos_str}'

if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    #print(producto1)
    producto2 = Producto('pantalon', 150.00)
    #print(producto2)
    canasta1 = [producto1,producto2]
    orden1 =  Orden(canasta1)
    print(orden1)
    canasta2 = [producto1,producto2]
    orden2 =  Orden(canasta2)
    print(orden2)