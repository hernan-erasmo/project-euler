"""El ejercicio plantea como que 28123 es el numero mas grande que
no puede ser escrito como suma de dos abundantes. Wikipedia reduce
ese numero a 20161"""

"""El ejercicio pide la suma de los numeros enteros que no pueden
expresarse como suma de abundantes"""

"""Entonces si yo quisiera encontrar un listado de numeros enteros
que no pueden expresarse como suma de abundantes, el numero mas
grande de ese listado seria 20161"""

"""Se me ocurre, 1) obtener un listado de abundantes hasta 20161, 
2) hacer las sumas entre todos (permutaciones, combinaciones, etc), 
lo que me da 3) un listado con los numeros que pueden expresarse
como suma de abundantes. 4) tomar el conjunto de numeros generado en
3 y hacer la diferencia con el conjunto de todos los numeros entre 1 
y 20161. 5) el conjunto diferencia, seria el conjunto de los numeros 
enteros	que no pueden expresarse como suma de abundantes, 6) realizar
la suma de los elementos de ese conjunto para obtener la respuesta"""

def es_abundante(n):
	return sum(mf.factores_de(n)[:-1]) > n

def main():
	abundantes = []
	for x in xrange(1,20162):
		if es_abundante(x):
			abundantes.append(x)

	cant = len(abundantes)
	print "Hay " + str(cant) + " abundantes"
	print "Serian",str(math.factorial(cant) / math.factorial(cant - 2)*math.factorial(2)),"sumas"

if __name__ == '__main__':
	import mis_funciones as mf
	import itertools as it
	import math
	main()
