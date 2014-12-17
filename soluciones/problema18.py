piramide = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def suma_piramide(piramide):
	lista_plana = [item for sublist in piramide for item in sublist]	#http://stackoverflow.com/a/952952/1603080
	return sum([int(x) for x in lista_plana])	

def main():
	"""El algoritmo funciona de la siguiente manera.
		(asumimos que la piramide tiene al menos un nivel, el cero, la raiz)
		0- Agregamos la raiz de la piramide al camino solucion.
		1- Si la piramide no tiene nivel 1, mostramos el camino solucion y salimos.
		2- Generamos dos piramides nuevas, cuyas raices son los numeros del nivel 1.
		3- Por cada piramide, calculamos la suma de todos los numeros que la componen.
		4- Tomamos como nueva piramide a aquella que tenga la suma mas grande.
			4.1- Si la suma es igual, tomamos la derecha, que es el camino de Dios.
		5- Volvemos al paso 0"""

	piramide_base = [x.split(' ') for x in piramide.split('\n')]
	camino_solucion = [piramide_base.pop(0)[0]]
	
	while len(piramide_base) > 1:
		piramide_izq = [piramide_base[i][:i+1] for i in range(len(piramide_base))]
		piramide_der = [piramide_base[i][-i-1:] for i in range(len(piramide_base))]

		if suma_piramide(piramide_izq) > suma_piramide(piramide_der):
			piramide_base = piramide_izq
		else:
			piramide_base = piramide_der

		camino_solucion.append(piramide_base.pop(0)[0])

	#Agregamos el elemento mas grande de la lista de 2 que nos queda al final
	ultimo_nivel = piramide_base.pop()
	camino_solucion.append(ultimo_nivel[0] if ultimo_nivel[0] > ultimo_nivel[1] else ultimo_nivel[1])

	print camino_solucion
	print "La suma es:", sum([int(x) for x in camino_solucion])

if __name__ == '__main__':
	main()
