class Empleado:
    
    def __init__(self,nombre,sueldo):
        if nombre != '' and float(sueldo) > 0:
            self._nombre = str(nombre)
            self._sueldo = float(sueldo)
        else:
            self._nombre = ''
            self._sueldo = 0


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def nombre(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Datos: {self._nombre}|{self._sueldo}'
