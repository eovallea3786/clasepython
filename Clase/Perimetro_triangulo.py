import math
def perimetro_triangulo(lado1,lado2,lado3):

    """
    (num)-> num

    Calculo del perimetro del triangulo

    >>> perimetro_triangulo(2,3,4)
    9

    >>> perimetro_triangulo(5,1,3)
    9

    >>> perimetro_triangulo(1,2,3)
    6

    :param lado1: Nùmero entero longitud del lado 1 de un triangulo
    :param lado2: Nùmero entero longitud del lado 2 de un triangulo
    :param lado3: Nùmero entero longitud del lado 3 de un triangulo
    :return: perimetro del triangulo
    """
    perimetro=lado1+lado2+lado3
    return perimetro

def semiperimetro_triangulo(lado1,lado2,lado3):

    """
    (num)-> num

    Calculo del semiperimetro del triangulo

    >>> semiperimetro_triangulo(2,3,4)
    4.5

    >>> semiperimetro_triangulo(5,1,3)
    4.5

    >>> semiperimetro_triangulo(1,2,3)
    3.0

    :param lado1: Nùmero entero longitud del lado 1 de un triangulo
    :param lado2: Nùmero entero longitud del lado 2 de un triangulo
    :param lado3: Nùmero entero longitud del lado 3 de un triangulo
    :return: semiperimetro del triangulo
    """

    return perimetro_triangulo(lado1,lado2,lado3)/2

def area_triangulo(lado1,lado2,lado3):
    """
    (num)-> num

    Calculo del area del triangulo

    >>> area_triangulo(2,3,4)
    2.9047375096555625

    >>> area_triangulo(5,5,3)
    7.1545440106270926

    >>> area_triangulo(5,2,4)
    3.799671038392666

    :param lado1: Nùmero entero longitud del lado 1 de un triangulo
    :param lado2: Nùmero entero longitud del lado 2 de un triangulo
    :param lado3: Nùmero entero longitud del lado 3 de un triangulo
    :return: area del triangulo
    """
    s=semiperimetro_triangulo(lado1, lado2, lado3)
    area= s*(s-lado1)*(s-lado2)*(s-lado3)
    area= math.sqrt(area)
    return area

def numero_impar(numero):
    """
    (num)->bool
    
    >>> numero_impar(3)
    True
    
    >>> numero_impar(5)
    True
    
    :param numero: Ingresa un numero
    :return: Retorna un boleano
    """

    return (numero % 2 != 0)

def numero_par(numero):
    """
    (num)->bool

    >>> numero_par(3)
    False

    >>> numero_par(2)
    True
    """

    return not numero_impar(numero)