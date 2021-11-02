class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        self._id_pruducto = Producto.incrementar_valor()
        self._nombre = nombre
        self._precio = precio

    @classmethod
    def incrementar_valor(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    @property
    def precio(self):
        return self._precio


    def __str__(self):
        return f'Producto: [{self._id_pruducto}]|{self._nombre}|{self._precio}'

if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    print(producto1)
    producto2 = Producto('pantalon', 150.00)
    print(producto2)
