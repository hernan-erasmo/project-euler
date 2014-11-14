"""Bueno, este fue medio con trampa. He tomado los valores de los resultados
(que no son repetidos) y los he puesto en el wolfram alpha, cuya sugerencia
fue que la secuencia era una binomial (2n n), entonces si n es 20..."""


"""Aunque, por otro lado, la solucion combinatoria es la mejor segun el pdf
del ejercicio (que obviamente vi despues de terminarlo). Asi que despues
de todo no fue tanto trampa... mas bien casualidad :/"""
def main():
	for x in range(1,6):
		l = [y for y in it.permutations("AD"*x)]
		print "Caminos posibles para una matriz de",str(x),"x",str(x),":"
		print "\tCon repetidos: ", len(l)
		print "\tSin repetidos: ", len(set(l))
		
	print "Como la secuencia sin repeticiones obedece a una binomial (2n n) -> "
	print "40! / (20! * 20!) -> ", math.factorial(40) / math.factorial(20)**2

if __name__ == '__main__':
	import math
	import itertools as it
	main()
