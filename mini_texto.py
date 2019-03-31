
def diminuir_texto(texto):
	tam = len(texto)
	texto_novo = ""
	if(tam > 15):
		for i in range(0,14):
			if i != 13:
				texto_novo += texto[i]
			else:
				texto_novo += "..."
	return texto_novo