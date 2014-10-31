def n_esmultiplode_m(n,m):
	return n % m == 0

def main():
	maximo = 1000
	lista = [x for x in range(1,maximo) if n_esmultiplode_m(x,3) or n_esmultiplode_m(x,5)]
	
	print "La respuesta es: " + str(sum(lista))

if __name__ == '__main__':
	main()
