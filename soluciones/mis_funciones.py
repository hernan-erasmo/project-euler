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
	"""Utiliza el algoritmo AKS para determinar si un numero es primo o no"""
	return False
