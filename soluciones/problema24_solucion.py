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
cadena = '0123456789'

def main():
	enesima_permutacion = calcular_enesima_permutacion(120)	#centesimo vigesima permutacion
	print factorizacion_por_frecuencias(1000000)

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
	
def calcular_enesima_permutacion(n):
	return 25

if __name__ == '__main__':
	import itertools
	main()
