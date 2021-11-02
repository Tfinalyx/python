class dispositivo_entrada:
	def __init__(self,tipo_entrada,marca):
		self._tipo_entrada = str(tipo_entrada)
		self._marca = str(marca)
		
	@property
	def tipo_entrada(self):
		return self._tipo_entrada
		
	@tipo_entrada.setter
	def tipo_entrada(self,tipo_entrada):
		_tipo_entrada = tipo_entrada
		
	@property
	def marca(self):
		return self._marca
		
	@tipo_entrada.setter
	def marca(self,marca):
		_marca = marca
		
	def __str__(self):
		return f'Datos: {self._tipo_entrada}|{self_.marca}'