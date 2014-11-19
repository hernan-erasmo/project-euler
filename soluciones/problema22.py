#necesita del archivo "names.txt"

def get_char_value(char):
	return ord(char) - ord('A') + 1

def get_alpha_value(cadena):
	return sum([get_char_value(char) for char in cadena])

def main():
	archivo = open('names.txt','r')
	nombres = archivo.readline().split(',')
	nombres = [nombre.replace('"','') for nombre in nombres]
	nombres.sort()

	print "La suma es:", sum([get_alpha_value(nombre)*(nombres.index(nombre) + 1) for nombre in nombres])

if __name__ == '__main__':
	main()
