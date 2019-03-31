# -*- coding: utf-8 -*-
from math import sqrt

def calcular(a, b, c):

	delta = (b**2) - 4 * a * c
	raiz_delta = sqrt(delta)
	if delta < 0:
		print("A equação não possui raízes reais")
	elif delta == 0:
		print("Raiz única - %.2f" % (-b + raiz_delta)/(2 * a))
	else:	 
		x1 = (-1 * b + raiz_delta) / (2 * a)
		x2 = (-1 * b - raiz_delta) / (2 * a)
		print("Raiz x' : %.2f" % x1)
		print("Raiz x'' : %.2f" % x2)