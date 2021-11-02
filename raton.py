from Dispositivo_Entrada import Dispositivo_Entrada

static contador_ratones = 0

class Raton:
	def __init__(self,tipo_entrada,marca):
		Dispositivo_Entrada.__init_(self, tipo_entrada, marca)
		self._id_raton = Raton.incrementar_contador()
	
	@classmetod 	
	def incrementar_contador(cls):
		cls.contador_ratones += 1
		return cls.contador_ratones
		
	def __str__(self):
		return f'Datos: {self._contador_ratones}|{Dipositivo_Entrada.__str__()}'
