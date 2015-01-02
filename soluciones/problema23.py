def main():
	# Lista de numeros que no pueden ser escritos como suma de dos abundantes
	# Secuencia OEIS A048242
	url = 'http://oeis.org/A048242/b048242.txt'
	texto = urllib.urlopen(url)
	suma = 0
	
	for line in texto:
		if line.strip():
			suma += int(line.strip().split(' ')[1])

	print suma

if __name__ == '__main__':
	import urllib
	main()
