import unittest
from Clase import Febrero as f

class pruebas(unittest.TestCase):

    def test_es_vocal(self):
        self.assertTrue(f.es_vocal('a'),True)
        self.assertTrue(f.es_vocal('e'),True)
        self.assertTrue(f.es_vocal('i'),True)
        self.assertTrue(f.es_vocal('o'),True)
        self.assertTrue(f.es_vocal('u'),True)
        self.assertFalse(f.es_vocal('aoo'),True)
        self.assertFalse(f.es_vocal('1'),True)
        self.assertFalse(f.es_vocal('abb'),True)



if __name__=='main':
    unittest.main()