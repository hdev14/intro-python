# -*- coding: utf-8 -*-

def votar():
	votos = []
	a = 0
	b = 0
	c = 0
	nulos = 0
	brancos = 0

	for i in range(15):
		print("%d - Eleitor\n" % i)
		votos.append(input("1 - Candidato A\n2 - Candidato B\n3 - Candidato C\n4 - Nulo\n5 - Branco\n"))

	for voto in votos:
		if voto != 4 and voto != 5:
			if voto == 1:
				a += 1
			elif voto == 2:
				b += 1
			else:
				c += 1
		else:
			if voto ==  4:
				nulos += 1
			else:
				brancos += 1

	print("Total A: %d \n" % a)
	print("Total B: %d \n" % a)
	print("Total C: %d \n" % a)
	print("Total Nulos : %d \n" % nulos)
	print("Total Brancos : %d \n" % brancos)
	print("Porcentagem votos nulos : %.1f " % ((nulos * 100)/15))
	print("Porcentagem votos brancos : %.1f " % ((brancos * 100)/15))