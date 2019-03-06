from unittest import TestCase

import Clase.ventiochofebrero as f

class TestCompara_edades(TestCase):

    def test_compara_edades(self):
        self.assertEqual(f.compara_edades(2, 3), "El segundo es mayor que el primero")
        self.assertEqual(f.compara_edades(3, 2), "El primero es mayor que el segundo")
        self.assertEqual(f.compara_edades(3, 3), "ambos tienen la misma edad")

