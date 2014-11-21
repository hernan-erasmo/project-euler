def main():
	encontrado = False
	cant_divisores = 0
	contador = count(1)

	while cant_divisores <= 500:
		triangular = mf.triangular_nro(contador.next())
		cant_divisores = len(mf.factores_de(triangular))
		print triangular, cant_divisores

if __name__ == '__main__':
	import mis_funciones as mf
	from itertools import count
	main()
