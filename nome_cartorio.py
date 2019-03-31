# -*- coding: utf-8 -*-

def formatarNome(nomeCompleto):
	nomes = [n.capitalize() for n in nomeCompleto.split()]
	nomeFormatado = " ".join(nomes)
	return nomeFormatado.replace(" Da ", " da ").replace(" De "," de ")
