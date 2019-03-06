def dividir(dividendo,divisor):
    """
    int, int -> float

    >>> dividir(6,2)
    3.0

    >>> dividir(4,2)
    2.0

    >>> dividir(5,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: No dividiras por 0, es el 11vo mandamiento

    >>> dividir('hola',100)
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero

    :param dividendo: Recibe dividendo
    :param divisor: Recibe divisor
    :return: resultado
    """

    if int != type(dividendo) != float:
        raise TypeError(str(dividendo)+ ' no es un numero')
    elif int != type(divisor) != float:
        raise TypeError(str(divisor)+ ' no es un numero')
    elif divisor==0:
        raise ZeroDivisionError('No dividiras por 0, es el 11vo mandamiento')
    return (dividendo/divisor)