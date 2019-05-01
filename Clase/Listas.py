def es_vocal(letra):

    """
    char -> str

    VALIDA SI UNA LETRA ES VOCAL


    >>> es_vocal('a')
    True

    >>> es_vocal('b')
    False

    >>> es_vocal('ad')
    Traceback (most recent call last):
    ..
    TypeError: ad no es una vocal

    >>> es_vocal('i')
    True

    :param letra: Ingresa una letra de tamaño 1
    :return: Retorna un booleano
    """

    if (len(letra) == 1 and letra.isalpha()):
        return letra in 'aeiouAEIOU'
    raise TypeError(letra + ' no es una vocal')


def contar_vocales(cadena):
    """
    char -> int
    Ingresa una cadena, retorna la cantidad de vocales en la cadena

    >>> contar_vocales('hola')
    2

    >>> contar_vocales('quiubo')
    4

    :param cadena: Ingresa una cadena de caracteres a evaluar
    :return: REtorna un entero evaluando la cantidad de vocales en la cadena
    """
    contador_vocal =0
    for letra in cadena:
        if es_vocal(letra):
            contador_vocal += 1
    return contador_vocal

def contar_letras(cadena):
    """
    char -> int
    Ingresa una cadena, retorna la cantidad de vocales en la cadena

    >>> contar_letras('hola')
    2

    >>> contar_letras('quiubo')
    2

    :param cadena: cadena a evaluar
    :return: sobrante de contar las vocales a comparacion de la longitud de cadena
    """
    return len(cadena)- contar_vocales(cadena)