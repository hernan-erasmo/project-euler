"""
Funciones auxiliares para resolver los problemas.

Algunas variables en este modulo pueden carecer de expresividad. He tratado
de ser expresivo cuando pude, sin embargo creo que en algunos algoritmos es
mejor utilizar las mismas letras que utiliza la wikipedia (o la fuente original,
en caso de que la aclare) para describir al algoritmo en cuestion"""

import math
import itertools
from random import randrange

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
	if n == 2:
		return True

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

def es_palindromo(n):
	"""Recibe un numero e indica si se lee igual al derecho que al reves"""
	return str(abs(n)) == str(abs(n))[::-1]		#http://stackoverflow.com/q/931092/1603080

def factor_pairs(n):
	"""Retorna una lista de pares de factores del nro n, sin repetidos"""
	return [(x,n/x) for x in xrange(1,n+1) if (n%x == 0) and (x < n/x)]

def dickson_triples(r):	#http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson.27s_method
	"""Genera una terna pitagorica a partir del nro r, utilizando el metodo de Dickson"""
	if (r < 0) or (r % 2 != 0):
		return []

	triples = []
	for p in factor_pairs((r**2)/2):
		s = p[0]
		t = p[1]
		x = r + s
		y = r + t
		z = r + s + t
		triples.append((x,y,z))

	return triples

def es_triangular(n):
	"""Un numero n es triangular si es el resultado de la suma de numeros naturales
	consecutivos contando a partir de 1"""
	acumulado = 0
	for i in xrange(n+1):
		acumulado += i
		if acumulado == n:
			return True

	return False

def triangular_nro(n):
	"""Retorna el n-esimo numero de la secuencia de numeros triangulares"""
	return (n*(n+1))/2

def collatz_sequence(start):
	if start >= 1:
		yield start

	n = start
	while n > 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n + 1
		
		yield n

def generadora_aleatorios(x,n):
	return (x**2 + randrange(x+n) + 1) % n

def pollard_rho_factor(n):
	"""Retorna un factor primo de n utilizando el algoritmo Pollard rho.
	Las variables estan tomadas de acuerdo a la pagina de wikipedia del algoritmo
	http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm#Algorithm"""
	
	if es_primo(n):
		return n

	semillero = itertools.count(2)
	x = y = semillero.next()
	d = 1
	encontrado = False

	while not encontrado:
		encontrado = True

		while d == 1:
			x = generadora_aleatorios(x,n)
			y = generadora_aleatorios(generadora_aleatorios(y,n),n)
			d = gdc(abs(x - y), n)

		if d == n:
			encontrado = False
			x = y = semillero.next()
			print x,y
			d = 1

	return d

def factores_primos_de(n):
	"""Utiliza pollard_rho_factor para retornar una lista de factores primos de n"""

	factor1 = pollard_rho_factor(n)
	factor2 = n / factor1
	factores = [factor1,factor2]
	respuesta = []

	while factores != []:
		factor = factores.pop()
		factor_mas_chico = pollard_rho_factor(factor)
		if factor == factor_mas_chico:
			respuesta.append(factor)
		else:
			factores.extend([factor_mas_chico, factor/factor_mas_chico])

	return respuesta
