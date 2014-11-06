def main():
	producto_max = 0
	rango = xrange(999,100,-1)
	p1 = 0
	p2 = 0

	for x, y in itertools.product(rango,rango):	#http://stackoverflow.com/q/11174745/1603080
		producto = x*y
		if mf.es_palindromo(producto):
			if producto > producto_max:
				producto_max = producto
				p1 = x
				p2 = y

	print "El palindromo mas grande producto de dos numeros de tres digitos es: " + str(producto_max) + " (" + str(p1) + "*" + str(p2) + ")"

if __name__ == '__main__':
	import mis_funciones as mf
	import itertools
	main()
