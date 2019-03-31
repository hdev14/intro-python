# -*- coding: utf-8 -*-

def eh_triangulo(a,b,c):
	if (a+b) >= c and (a+c) >= b and (b+c) >= a:
		print("Triangulo !")
	else:
		print("Não é triangulo !")