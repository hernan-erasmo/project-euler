import math

def n_esmultiplode_m(n,m):
	return n % m == 0

def phi():
	return (1 + math.sqrt(5))/2

def fib(n):
	"""Utiliza la formula de Binet para encontrar el n-esimo numero de la sucesion de Fibonacci"""
	numerador = phi()**n - ((-1)*(phi()))**(n*(-1))
	denominador = math.sqrt(5)
	return int(numerador / denominador)

def es_primo(n):
	"""Utiliza el test AKS para determinar si un numero es primo o no"""
	if n <= 1:			#Primer paso del AKS
		return False
	if es_potencia(n):	#Segundo paso del AKS
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
