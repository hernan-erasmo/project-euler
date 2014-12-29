fib_inicial = [1,1]		#Primeros dos numeros de la secuencia de Fibonacci

def main():
	lista = fib_inicial
	indice = 1
	tope = 10**999

	for n in itertools.count(start=1,step=1):
		lista.append(lista[0]+lista[1])
		del(lista[0])
		indice += 1

		if (lista[0] >= tope) or (lista[1] >= tope):
			break

	print "La lista contiene los elementos {0}({1} caracteres) y {2}({3} caracteres) de la secuencia.".format(indice, len(str(lista[0])), indice + 1,len(str(lista[1])))
	print lista

if __name__ == '__main__':
	import itertools
	main()
