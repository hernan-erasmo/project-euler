#Calcado del problema 16

def main():
	print "La respuesta es: ", sum([int(x) for x in str(factorial(100))])	#Que groso, Python!

if __name__ == '__main__':
	from math import factorial
	main()
