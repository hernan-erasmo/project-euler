def main():
	fib_inicial = [1,1]		#Primeros dos numeros de la secuencia de Fibonacci
	lista = fib_inicial
	tope = 10**999

	for n in itertools.count(start=1,step=1):
		lista.append(lista[0]+lista[1])
		del(lista[0])

		if (lista[0] >= tope) or (lista[1] >= tope):
			break

	print "La respuesta es", n + len(fib_inicial)

if __name__ == '__main__':
	import itertools
	main()
