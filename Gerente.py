from Empleado import Empleado

class Gerente:

    def __init__(self, nombre, sueldo, departamento):
        self._departamento = departamento
        Empleado.__init__(self,nombre, sueldo)


    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento


    def __str__(self):
        return f'Datos: {Empleado.__str__(self)}|{self._departamento}'
