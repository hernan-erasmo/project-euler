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

piramide_base = [x.split(' ') for x in piramide.split('\n')]

def get_secuencia(camino):
	"""Crea la secuencia de numeros que corresponden al camino indicado, incluyendo la raiz,
	y los convierte a numeros.
	0 = el camino va hacia la izquierda
	1 = el camino va hacia la derecha"""
	
	indice_anterior = 0
	resultado = [piramide_base[0][0]]

	for nivel,direccion in enumerate(camino, start=1):
		if direccion == '0':
			puntero = indice_anterior
		else:
			puntero = indice_anterior + 1

		indice_anterior = puntero
		resultado.append(piramide_base[nivel][puntero])

	return [int(x) for x in resultado]

def main():
	camino_max = ''
	suma_max = 0

	for x in xrange(2**14):
		secuencia = get_secuencia(bin(x)[2:].zfill(14))
		suma = sum(secuencia)

		if suma > suma_max:
			suma_max = suma
			camino_max = secuencia

	print camino_max, suma_max

if __name__ == '__main__':
	main()
