from unittest import TestCase

from Clase import esparentesis as f


class TestEsparentesis(TestCase):
    def test_esparentesis(self):
        self.assertEqual(f.esparentesis(')'), 'Es parentesis')
        self.assertEqual(f.esparentesis('('), 'Es parentesis')
        self.assertEqual(f.esparentesis('a'), 'No es parentesis')
