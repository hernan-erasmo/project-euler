fib_inicial = [1,1]		#Primeros dos numeros de la secuencia de Fibonacci

def main():
	lista = fib_inicial
	indice = 1

	for n in itertools.count(start=1,step=1):
		lista.append(lista[len(lista)-1]+lista[len(lista)-2])
		del(lista[0])
		indice += 1

		if (len(str(lista[0])) or len(str(lista[1]))) >= 1000:
			break

	print "La lista contiene los elementos {0} y {1} de la secuencia.".format(indice, indice + 1)
	print lista
	print "Los numeros tienen una longitud de {0} y {1} caracteres.".format(len(str(lista[0])),len(str(lista[1])))

if __name__ == '__main__':
	import itertools
	main()
