unidades = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 
7:'seven', 8:'eight', 9:'nine'}

decenas = {10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 
60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

especiales = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 
15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

centenas = {100:'one hundred', 200:'two hundred', 300:'three hundred', 
400:'four hundred', 500:'five hundred', 600:'six hundred', 700:'seven hundred',
800:'eight hundred', 900:'nine hundred'}

def palabra_unidad(n):
	return unidades[n]

def palabra_decena(n):
	digito_decena = n / 10
	unidad = n % 10
	decena = digito_decena * 10
	
	if n in range(11,20):
		return especiales[n]

	if unidad == 0:
		return decenas[decena]
	else:
		return decenas[decena] + "-" + itow(unidad)

def palabra_centena(n):
	resto = n % 100

	if resto == 0:
		return centenas[n]
	else:
		return centenas[n - resto] + " and " + itow(resto)

def itow(n):
	if n in range(1,10):
		return unidades[n]
	elif n in range(10,100):
		return palabra_decena(n)
	else:
		return palabra_centena(n)
	
def main():
	de_1_a_999 = "".join([itow(x) for x in range(1,1000)])
	mil = de_1_a_999 + "onethousand"
	cadena_limpia = mil.replace("-","").replace(" ","")
	
	print "En la cadena hay", len(cadena_limpia), "letras."
	
if __name__ == '__main__':
	main()
