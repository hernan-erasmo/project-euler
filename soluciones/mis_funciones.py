"""
Funciones auxiliares para resolver los problemas.

Algunas variables en este modulo pueden carecer de expresividad. He tratado
de ser expresivo cuando pude, sin embargo creo que en algunos algoritmos es
mejor utilizar las mismas letras que utiliza la wikipedia (o la fuente original,
en caso de que la aclare) para describir al algoritmo en cuestion"""

import math
import itertools

def n_esmultiplode_m(n,m):
	return n % m == 0

def phi():
	return (1 + math.sqrt(5))/2

def euler_phi(n):
	"""Retorna la cantidad de enteros k, tales que 1 < k <= n, y gdc(k,n) = 1"""
	cant = 0
	for k in range(1,n+1):
		if gdc(k,n) == 1:
			cant += 1

	return cant

def fib(n):
	"""Utiliza la formula de Binet para encontrar el n-esimo numero de la sucesion de Fibonacci"""
	numerador = phi()**n - ((-1)*(phi()))**(n*(-1))
	denominador = math.sqrt(5)
	return int(numerador / denominador)

def es_primo(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(math.floor(math.sqrt(n))) + 1):
		if n % i == 0:
			return False

	return True

def es_potencia(n):
	"""Verifica si n puede expresarse como base**exp con base y exp enteros > a 1"""
	pot = 0
	tope = int(math.sqrt(n)) + 1

	for base in range(2,tope + 1):
		for exp in range(2,tope + 1):
			pot = base**exp
			if n == pot:
				return True
			if pot > n:
				break
	return False

def son_congruentes_modulo(a,b,n):
	"""Verifica si a y b son congruentes modulo n"""
	return n_esmultiplode_m(a-b,n)

def gdc(a,b):
	"""Calcula el maximo comun divisor entre a y b"""
	if b == 0:
		return a
	else:
		return gdc(b, a % b)

def orden_multiplicativo(n,r):
	"""Calcula el orden multiplicativo de n modulo r.
	   Si gdc(n,r) != 1, no se puede calcular el orden multiplicativo.
	   Los valores a, n y k se tomaron de la definicion de wikipedia"""
	if gdc(n,r) != 1: return -1

	contador = itertools.count(1)
	while True:
		k = contador.next()
		if son_congruentes_modulo(n**k, 1, r):
			return k

def buscar_factor_impar(n):
	"""Retorna el factor impar mas alto de n"""
	if n % 2 != 0:
		return n
	else:
		return buscar_factor_impar(n / 2)
