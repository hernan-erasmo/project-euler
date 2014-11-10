"""Se va notando la baja performance de es_primo con numeros altos.
Si sigue habiendo ejercicios de numeros primos cada vez mas grandes, va a 
haber que ir pensando en una implementacion mas rapida"""

def main():
	n = 3
	suma = 0
	while n < 2000000:
		if mf.es_primo(n):
			print n
			suma += n

		n += 2

	print "Suma: " + str(suma + 2)

if __name__ == '__main__':
	import mis_funciones as mf
	main()
