import unittest
import mis_funciones as mf

class TestMisFunciones(unittest.TestCase):
	def test_es_primo(self):
		self.assertFalse(mf.es_primo(256))
		self.assertFalse(mf.es_primo(50))
		self.assertTrue(mf.es_primo(2))
		self.assertTrue(mf.es_primo(7))
		self.assertTrue(mf.es_primo(3950827))

	def test_es_potencia(self):
		self.assertTrue(mf.es_potencia(8))

	def test_es_palindromo(self):
		self.assertTrue(mf.es_palindromo(1498941))
		self.assertTrue(mf.es_palindromo(2))
		self.assertTrue(mf.es_palindromo(-29892))
		self.assertFalse(mf.es_palindromo(9283539))

	def test_es_triangular(self):
		self.assertTrue(mf.es_triangular(28))
		self.assertTrue(mf.es_triangular(1))
		self.assertFalse(mf.es_triangular(514))
		self.assertFalse(mf.es_triangular(-1))

	def test_triangular_nro(self):
		self.assertEquals(mf.triangular_nro(7),28)
		self.assertEquals(mf.triangular_nro(6),21)
		self.assertEquals(mf.triangular_nro(1200),720600)

	def test_son_congruentes_modulo(self):
		self.assertTrue(mf.son_congruentes_modulo(38,14,12))
		self.assertTrue(mf.son_congruentes_modulo(-10,40,25))
		self.assertFalse(mf.son_congruentes_modulo(50,-10,9))

	def test_gdc(self):
		self.assertEquals(mf.gdc(20,30),10)
		self.assertEquals(mf.gdc(-20,50),10)
		self.assertEquals(mf.gdc(4,7),1) # coprimos
		self.assertEquals(mf.gdc(900,59),1)	# coprimos
		self.assertEquals(mf.gdc(284,1611),1)	# coprimos

	def test_orden_multiplicativo(self):
		self.assertEquals(mf.orden_multiplicativo(10,5),-1) #No se puede calcular
		self.assertEquals(mf.orden_multiplicativo(4,7), 3)
		self.assertEquals(mf.orden_multiplicativo(900,59), 29)
		self.assertEquals(mf.orden_multiplicativo(284,1611), 534)

	def test_euler_phi(self):
		self.assertEquals(mf.euler_phi(9),6)
		self.assertEquals(mf.euler_phi(3496),1584)

	def test_buscar_factor_impar(self):
		self.assertEquals(mf.buscar_factor_impar(80),5)
		self.assertEquals(mf.buscar_factor_impar(10000),625)
		self.assertEquals(mf.buscar_factor_impar(49),49)
		self.assertEquals(mf.buscar_factor_impar(199543),199543)

	def test_factor_pairs(self):
		self.assertEquals(mf.factor_pairs(18),[(1,18),(2,9),(3,6)])
		self.assertEquals(mf.factor_pairs(-5),[])
		self.assertEquals(mf.factor_pairs(10111),[(1,10111)])

	def test_dickson_triples(self):
		self.assertEquals(mf.dickson_triples(-4), [])
		self.assertEquals(mf.dickson_triples(6), [(7,24,25), (8,15,17), (9,12,15)])

	def test_collatz_sequence(self):
		self.assertEquals([x for x in mf.collatz_sequence(13)], [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
		self.assertEquals([x for x in mf.collatz_sequence(3)], [3, 10, 5, 16, 8, 4, 2, 1])
		self.assertEquals([x for x in mf.collatz_sequence(1)], [1])
		self.assertEquals([x for x in mf.collatz_sequence(-2)], [])

if __name__ == '__main__':
	unittest.main()
