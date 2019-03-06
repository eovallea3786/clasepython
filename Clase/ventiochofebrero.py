import datetime

"""

nombre=input('Cual es tu nombre ')
amigo= input('Como se llama tu amigo ')

print("tu amigo se llama {1} y tu te llamas {0}".format(nombre,amigo))
"""

def flotante(decimal):

    """

    float -> str

    La funcion verifica un numero decimal si es mayor que 0 o no

    >>> flotante(10.0)
    El numero es un numero positivo

    >>> flotante(-2.0)
    El numero es un numero negativo porque es menor que 0

    :param decimal: numero flotante
    :return:str con el mensaje de evaluaciòn
    """

    if decimal<0:
        return ("El numero es un numero negativo porque es menor que 0 ")
    return ("El numero es un numero positivo")

def compara_edades(edad1,edad2):
    """
    int1,int2-> bool

    Compara dos numero enteros. y retorna un str

    >>> compara_edades(2,3)
    El primero es mayor que el segundo

    >>> compara_edades(3,2)
    El segundo es mayor que el primero

    >>> compara_edades(3,3)
    ambos tienen la misma edad

    >>>
    :param edad1: entero 1
    :param edad2: entero 2
    :return: str de evaluacion
    """
    if (edad1>edad2):
        return ("El primero es mayor que el segundo")
    elif (edad2>edad1):
        return ("El segundo es mayor que el primero")
    return ("ambos tienen la misma edad")
