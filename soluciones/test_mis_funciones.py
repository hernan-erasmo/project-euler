import unittest
import mis_funciones as mf

class TestMisFunciones(unittest.TestCase):
	def test_es_primo(self):
		self.assertFalse(mf.es_primo(256))
		self.assertTrue(mf.es_primo(255))

	def test_es_potencia(self):
		self.assertTrue(mf.es_potencia(8))

if __name__ == '__main__':
	unittest.main()
