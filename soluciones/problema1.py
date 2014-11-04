def main():
	maximo = 1000
	lista = [x for x in range(1,maximo) if mf.n_esmultiplode_m(x,3) or mf.n_esmultiplode_m(x,5)]
	
	print "La respuesta es: " + str(sum(lista))

if __name__ == '__main__':
	import mis_funciones as mf
	main()
