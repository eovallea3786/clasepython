from unittest import TestCase

import Clase.ventiochofebrero as f


class TestFlotante(TestCase):
    def test_flotante(self):
        self.assertEqual(f.flotante(2.0), "El numero es un numero positivo")
        self.assertEqual(f.flotante(-2.0), "El numero es un numero negativo porque es menor que 0 ")

