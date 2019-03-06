import math
def area_circulo(radio):
    """
    (num) -> float

    Calcula el area del triangulo


    >>> area_circulo(3)
    9.42477796076938
    >>> area_circulo(2)
    6.283185307179586

    :param radio: Float numero radio del circulo
    :return: area del circulo
    """

    area = radio * math.pi
    return area