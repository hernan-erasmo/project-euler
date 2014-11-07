def main():
	rango = range(1,101)
	suma_cuadrados = sum([x**2 for x in rango])
	cuadrado_suma = sum([x for x in rango])**2
	
	print "La respuesta es: " + str(cuadrado_suma - suma_cuadrados)

if __name__ == '__main__':
	main()
