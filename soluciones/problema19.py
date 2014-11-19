def main():
	inicio = datetime.date(1901,1,1)	#inicio.isoweekday() == 2, martes
	fin = datetime.date(2000,12,31)		#fin.isoweekday() == 7, domingo
	domingos_primero_de_mes = 0
	semana = datetime.timedelta(days=7)

	#Nos paramos en el primer domingo
	dia_actual = inicio + datetime.timedelta(days=5)

	#dia_actual siempre sera domingo
	while dia_actual <= fin:
		if dia_actual.day == 1:
			domingos_primero_de_mes += 1
			print dia_actual, "(Domingo 1ro!)"
		
		dia_actual += semana

	print "Cantidad de domingos 1ro de mes durante el siglo XX:", str(domingos_primero_de_mes)

if __name__ == '__main__':
	import datetime
	main()
