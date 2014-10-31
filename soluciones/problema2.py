def phi():
	return (1 + math.sqrt(5))/2

def fib(n):
	"""Utiliza la formula de Binet para encontrar el n-esimo numero de la sucesion"""
	numerador = phi()**n - ((-1)*(phi()))**(n*(-1))
	denominador = math.sqrt(5)
	return int(numerador / denominador)

def main():
	nro_grande = 300	#Suficientemente grande para que la comprehension corte por la condicion 'if' en lugar de por el range
	tope_projecteuler = 4000000
	fibos = [fib(x) for x in range(1,nro_grande) if fib(x) < tope_projecteuler]
	fibos_pares = [x for x in fibos if x % 2 == 0]
	print "La respuesta es: " + str(sum(fibos_pares))

if __name__ == '__main__':
	import math
	main()
