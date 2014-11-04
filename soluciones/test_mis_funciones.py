import unittest
import mis_funciones as mf

class TestMisFunciones(unittest.TestCase):
	def test_es_primo(self):
		return self.assertFalse(mf.es_primo(6))

if __name__ == '__main__':
	unittest.main()
