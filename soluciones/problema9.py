def main():
	r = 2
	encontrada = False
	while not encontrada:
		for t in mf.dickson_triples(r):
			print "r = " + str(r) + " - Probando con ", t, " (suma: " + str(t[0] + t[1] + t[2]) + ")"
			if (t[0] + t[1] + t[2]) == 1000:
				print "La terna es: ", t, " y el producto de las componentes es: " + str(t[0]*t[1]*t[2])
				encontrada = True
				break

		r += 2

if __name__ == '__main__':
	import mis_funciones as mf
	main()
