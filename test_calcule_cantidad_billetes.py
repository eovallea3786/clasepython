from unittest import TestCase

import Ejercicios as f


class TestEs_parentesis(TestCase):
    def test_es_parentesis(self):
        self.assertEqual(f.es_parentesis(')'), 'Es parentesis')
        self.assertEqual(f.es_parentesis('a'),'No es parentesis')
        self.assertRaises(TypeError,f.es_parentesis, 'xa no es un parentesis')

class TestNumero_primo(TestCase):
    def test_numero_primo(self):
        self.assertEqual(f.numero_primo(2),'2 Es un numero primo')
        self.assertEqual(f.numero_primo(4), '4 No es un numero primo')
        self.assertEqual(f.numero_primo(0), '0 No es un numero primo')
        self.assertRaises(TypeError, f.numero_primo, 'hola no es un numero o otro tipo de caracter')

class TestCalcule_cantidad_billetes(TestCase):
    def test_calcule_cantidad_billetes(self):
        self.assertEqual(f.calcule_cantidad_billetes(2500), ' Usted requiere 6 billetes de 500, Usted requiere 1 billetes de 200, Usted requiere 1 billetes de 100,')
        self.assertEqual(f.calcule_cantidad_billetes('hola'), "El segundo es mayor que el primero")
        self.assertEqual(f.calcule_cantidad_billetes('6.2'), "6.2 no es un numero o otro tipo de caracter")
        self.assertEqual(f.calcule_cantidad_billetes('-600'), "-600 no es un valor para una cantidad monetaria")