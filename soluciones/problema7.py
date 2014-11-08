def main():
	i = 1
	contador_primos = 0	

	while contador_primos < 10001:
		if mf.es_primo(i):
			contador_primos += 1
			print "Primo nro " + str(contador_primos) + ": " + str(i)
		i += 2

if __name__ == '__main__':
	import mis_funciones as mf
	main()
