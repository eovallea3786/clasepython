def esparentesis(caracter):
    """
    5 de Marzo del 2019

    (string of len ==1) -> string

    Funcion que define si un caracter es Parentesis

    >>> esparentesis('(')
    'Es parentesis'

    >>> esparentesis(')')
    'Es parentesis'

    >>> esparentesis('a')
    'No es parentesis'

    :param caracter: Ingresa caracter
    :return: Mensaje si es o no parentesis
    """

    if ((caracter)=='('):
        return 'Es parentesis'
    elif ((caracter)==')'):
        return 'Es parentesis'
    else:
        return 'No es parentesis'