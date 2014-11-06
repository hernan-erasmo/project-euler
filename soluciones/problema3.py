def main():
	factor_max = 2
	n = 600851475143
	tope = int(math.floor(math.sqrt(n)))

	for i in range(2, tope + 1):
		if (n % i == 0) and (mf.es_primo(i)):
			if i > factor_max:
				factor_max = i

	print "El factor primo mas alto de n = " + str(n) + " es: " + str(factor_max)

if __name__ == '__main__':
	import math
	import mis_funciones as mf
	main()
