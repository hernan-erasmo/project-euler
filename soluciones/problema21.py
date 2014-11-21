def main():
	pares = []
	tope = 10000
	dominio = [x for x in range(1, tope+1)]
	
	for item in dominio:
		suma1 = sum(mf.factores_de(item)[:-1])
		if suma1 >= tope:
			continue
		
		suma2 = sum(mf.factores_de(suma1)[:-1])
		if item == suma2 and item != suma1:
			pares.append((item,suma1))

	pares = set(((a,b) if a<=b else (b,a) for (a,b) in pares))
	print "Amigables", pares

	suma = 0
	for p in pares:
		suma += p[0] + p[1]

	print "La suma de todos es:", suma


if __name__ == '__main__':
	import mis_funciones as mf
	main()
