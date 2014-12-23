"""Esta es una solucion bien catinga. Observando los patrones de cambio
de los numeros que se permutan y de las posiciones de esos numeros, noto
que sobre las distintas columnas (de la 0 a la 9) los numeros cambian con
distinta frecuencia. Dicha frecuencia es:
	Para los numeros de la columna N		Cambia cada M lugares
				9										1
				8										1
				7										2
				6										6
				5										24
				4										120
				3										720
				2										5040
				1 										40320
				0										362880

Esta es una secuencia de factorial descendente (buscar Pochhammer Symbol en wikipedia)
Este programa es simplemente una implementacion del calculo a mano de la millonesima
permutacion lexicografica utilizando estos datos de frecuencia.
"""
frecs_cambio = [362880,40320,5040,720,120,24,6,2,1,1]
cadena_ejercicio = '0123456789'

def main():
	frecuencias = factorizacion_por_frecuencias(1000000)
	"""
	c = cadena
	For f in frecuencias:
			c = incrementar_posicion_n_lugares(c,f[a],f[b])
	"""
	print frecuencias

def factorizacion_por_frecuencias(n):
	return [x for x in generar_factorizacion(n)]

def generar_factorizacion(n):
	while n is not 0:
		multiplicador = 0
		for frec in frecs_cambio:
			multiplicador = n / frec
			if multiplicador > 0:
				n -= frec * multiplicador
				yield (frec, multiplicador)
				break
	
def incrementar_posicion_n_lugares(cadena,pos,cant):
	"""Incrementa la posicion 'pos' de la 'cadena' una cantidad de lugares 'cant' y 
	retorna la cadena resultado. Hay que ordenar los lugares posteriores al cambio de
	menor a mayor:
	Ejemplo:
			asdf = incrementar_posicion_n_lugares('0123',1,2)
			>>>> asdf
			>>>> '0312'

			asdf = incrementar_posicion_n_lugares('0123456',2,3)
			>>>> asdf
			>>>> '0152346'
	"""


if __name__ == '__main__':
	import itertools
	main()
