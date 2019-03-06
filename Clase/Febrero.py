def es_vocal(letra):
    """
    str (len(1)) -> bool

    Determina si una letra es vocal

    >>> es_vocal('a')
    True

    >>> es_vocal('b')
    False

    :param letra: letra str la letra a evaluar
    :return: True si es una vocal
    """
    return len (letra)== 1 and letra in 'aeiouAEIOU'