"""Esta solucion, por mas que sea medio bruta, termina en solo 6.2 segundos.
   Si tengo tiempo implemento alguna mas copada (aunque 6.2 s. esta bastante bien!)"""

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
