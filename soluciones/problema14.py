"""Podria ser mucho mas rapido si se pudiera identificar a un x intermedio como
un numero en una secuencia ya calculada. En ese caso, solo habria que unir la
lista que se esta calculando actualmente con la que ya se habia calculado antes"""

def main():
	max_len = 0
	for n in xrange(1, 1000001):
		seq = [x for x in mf.collatz_sequence(n)]
		len_seq = len(seq)
		if len_seq > max_len:
			max_len = len_seq
			print "Hasta ahora, la mas larga tiene " + str(max_len) + " y es ", seq

if __name__ == '__main__':
	import mis_funciones as mf
	main()
