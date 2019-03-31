# -*- coding: utf-8 -*-

def calcular():
	string = '''
		1 - Soma
		2 - Subtração
		3 - Multiplicação
		4 - Divisão
	'''
	print("%s" % string)

	op = input("Opção:\n")
	n1 = input("Primeiro valor:\n")
	n2 = input("Segundo valor:\n")

	try:

		if op == 1:
			print("Somar => %d" % (n1 + n2))
		elif op == 2:
			print("Subtração => %d" % (n1 - n2))
		elif op == 3:
			print("Multiplicação => %d" % (n1 * n2))
		else:
			print("Divisão => %.1f" % (n1 / n2))
			
	except:
		print("Opção ou valor inválido !")

