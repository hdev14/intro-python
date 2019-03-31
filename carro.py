class Carro():

	def __init__(self, consumo, capacidade):
		self.consumo = consumo
		self.capacidade = capacidade
		self.combustivel = 0

	def mover(self, km):
		litros_gastados = km * self.consumo
		if self.combustivel >= litros_gastados:
			self.combustivel -= litros_gastados
		else:
			self.combustivel = 0


	def gasolina(self):
		return self.combustivel

	def abastecer(self, litros):
		if self.combustivel < self.capacidade and (self.combustivel + litros) <= self.capacidade:
			self.combustivel += litros
		else:
			print("Tanque cheio!")

