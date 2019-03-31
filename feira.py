# -*- coding: utf-8 -*-

def venda():
	morangos = int(input("Quantos morangos?"))
	macas = int(input("Quantos maçãs?"))
	valor = 0.0

	try:
		if morangos <= 5 and morangos > 0:
			valor += 2.5 * morangos 
		else:
			valor += 2.2 * morangos

		if macas <= 5 and macas > 0:
			valor += 1.8 * macas 
		else:
			valor += 1.5 * macas

		if valor > 25.0 or (morangos + macas) > 8:
			valor -= 0.1 * valor

		print("Valor: %.2f" % valor)
	except:
		print("Valores inválidos!")