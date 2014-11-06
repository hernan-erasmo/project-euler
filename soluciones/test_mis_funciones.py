import unittest
import mis_funciones as mf

class TestMisFunciones(unittest.TestCase):
	def test_es_primo(self):
		self.assertFalse(mf.es_primo(256))
		self.assertFalse(mf.es_primo(50))
		self.assertTrue(mf.es_primo(7))
		self.assertTrue(mf.es_primo(3950827))

	def test_es_potencia(self):
		self.assertTrue(mf.es_potencia(8))

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

if __name__ == '__main__':
	unittest.main()
