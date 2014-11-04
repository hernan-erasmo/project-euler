def main():
	nro_grande = 300	#Suficientemente grande para que la comprehension corte por la condicion 'if' en lugar de por el range
	tope_projecteuler = 4000000
	fibos = [mis_funciones.fib(x) for x in range(1,nro_grande) if mis_funciones.fib(x) < tope_projecteuler]
	fibos_pares = [x for x in fibos if x % 2 == 0]
	print "La respuesta es: " + str(sum(fibos_pares))

if __name__ == '__main__':
	import mis_funciones
	main()
