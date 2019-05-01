from unittest import TestCase

import Ejercicios as f

class TestMensaje_negativo(TestCase):
    def test_mensaje_negativo(self):
        self.assertEqual(f.mensaje_negativo(-10.0), 'El numero es negativo')
        self.assertEqual(f.mensaje_negativo(898), 'El numero es positivo')

class TestCompara_edades(TestCase):
    def test_compara_edades(self):
        self.assertEqual(f.compara_edades(10, 20), 'El primero es mas joven')
        self.assertEqual(f.compara_edades(89, 56), 'El segundo es mas joven')
        self.assertEqual(f.compara_edades(56, 56), 'Tienen la misma edad')

class TestEs_parentesis(TestCase):
    def test_es_parentesis(self):
        self.assertEqual(f.es_parentesis(')'), 'Es parentesis')
        self.assertEqual(f.es_parentesis('a'),'No es parentesis')
        self.assertRaises(TypeError,f.es_parentesis, 'xa no es un parentesis')

class TestDividir(TestCase):
    def test_dividir(self):
        self.assertEqual(f.dividir(6,2), 3.0)
        self.assertRaises(TypeError,f.dividir, 'hola no es un numero')

class TestDoble_impar(TestCase):
    def test_doble_impar(self):
        self.assertEqual(f.doble_impar(14),'la mitad del numero 14 ingresado es un numero impar')
        self.assertEqual(f.doble_impar(12), 'la mitad del numero 12 ingresado no es un numero impar')
        self.assertEqual(f.doble_impar(0), 'la mitad del numero 0 ingresado no es un numero impar')
        self.assertRaises(TypeError,f.doble_impar, 'hola no es un numero o otro tipo de caracter')
        self.assertRaises(TypeError,f.doble_impar, '6.2 no es un numero o otro tipo de caracter')

class comparar_cuadrado(TestCase):
    def comparar_cuadrado(self):
        self.assertEqual(f.compara_edades(2,4), 'El segundo es el cuadrado del primero')
        self.assertEqual(f.compara_edades(2, 3), 'El segundo es menor que el cuadrado del primero')
        self.assertEqual(f.compara_edades(2, 5), 'El segundo es mayor que el cuadrado del primero')
        self.assertRaises(TypeError,f.comparar_cuadrado, 'Alguno de los dos numeros ingresados no es un numero o otro tipo de caracter')
        self.assertRaises(TypeError, f.comparar_cuadrado,
                          'Alguno de los dos numeros ingresados no es un numero o otro tipo de caracter')

class TestNumero_primo(TestCase):
    def test_numero_primo(self):
        self.assertEqual(f.numero_primo(2),'2 Es un numero primo')
        self.assertEqual(f.numero_primo(4), '4 No es un numero primo')
        self.assertEqual(f.numero_primo(0), '0 No es un numero primo')
        self.assertRaises(TypeError, f.numero_primo, 'hola no es un numero o otro tipo de caracter')

class TestCalcule_cantidad_billetes(TestCase):
    def test_calcule_cantidad_billetes(self):
        self.assertEqual(f.calcule_cantidad_billetes(3300), ' Usted requiere 6 billetes de 500, Usted requiere 1 billetes de 200, Usted requiere 1 billetes de 100,')
        self.assertRaises(TypeError, f.calcule_cantidad_billetes, "El segundo es mayor que el primero")
        self.assertRaises(TypeError, f.calcule_cantidad_billetes, "6.2 no es un numero o otro tipo de caracter")
        self.assertRaises(TypeError, f.calcule_cantidad_billetes, "-600 no es un valor para una cantidad monetaria")

