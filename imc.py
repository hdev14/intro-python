# -*- coding: utf-8 -*-

def imc(height, width):

	try:

		imc = width/height**2

		if imc < 16:
			print("Magreza grave - IMC %f" % imc)
		elif imc >= 16 and imc < 17:
			print("Magreza moderada - IMC %f" % imc)
		elif imc >= 17 and imc < 18.5:
			print("Magreza leve - IMC %f" % imc)
		elif imc >= 18.5 and imc < 25:
			print("Saudável - IMC %f" % imc)
		elif imc >= 25 and imc < 30:
			print("Sobrepeso - IMC %f" % imc)
		elif imc >= 30 and imc < 35:
			print("Obesidade Grau I - IMC %f" % imc)
		elif imc >= 35 and imc < 40:
			print("Obesidade Grau II - IMC %f" % imc)
		else:
			print("Obesidade Grau III - IMC %f" % imc)
	except:
		print("Valor inválido")