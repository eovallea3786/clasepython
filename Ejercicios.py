def mensaje_negativo(numero):
    """
    (float) -> str

    Escribe un mensaje para evaluar un numero negativo

    >>> mensaje_negativo(-10.0)
    'El numero es negativo'

    >>> mensaje_negativo(898)
    'El numero es positivo'

    :param numero: num el numero a evaluar
    :return: str con el mensaje de la evaluación
    """
    if numero < 0:
        return 'El numero es negativo'
    return 'El numero es positivo'

def compara_edades(edad1, edad2):
    """
    (int, int) -> str

    Genera un mensaje segun la diferencia de edad:
    la primera o la segunda mas joven o iguales

    >>> compara_edades(10, 20)
    'El primero es mas joven'

    >>> compara_edades(89, 56)
    'El segundo es mas joven'

    >>> compara_edades(56, 56)
    'Tienen la misma edad'

    :param edad1: int la edad del primero
    :param edad2: int la edad del segundo
    :return: mensaje asociado a la diferencia de edad
    """
    if edad1 > edad2:
        return 'El segundo es mas joven'
    elif edad1 == edad2:
        return 'Tienen la misma edad'
    else:
        return 'El primero es mas joven'


def es_parentesis(caracter):
    """

    (str of len == 1) -> str

    >>> es_parentesis('(')
    'Es parentesis'
    >>> es_parentesis('x')
    'No es parentesis'
    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """
    if len(caracter) != 1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter == ')':
        return 'Es parentesis'
    return 'No es parentesis'


def dividir(dividendo, divisor):
    '''

    (num, num) -> num

    Divide un numero entre otro

    >>> dividir(6, 2)
    3.0
    >>> dividir(1,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: No dividiras por 0
    >>> dividir('hola', 100)
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero

    :param dividendo: num el dividendo a evaluar
    :param divisor: num el divisor a evaluar
    :return: la división entre dividendo y divisor
    '''
    if  int != type(dividendo) != float:
        raise TypeError(str(dividendo) + ' no es un numero')
    elif int != type(divisor) != float:
        raise TypeError(str(divisor) + ' no es un numero')
    elif divisor == 0:
        raise ZeroDivisionError('No dividiras por 0')
    return dividendo / divisor

def doble_impar(numero):
    """

    int-> str

    Calcula si el nùmero ingresado es el doble de un nùmero impar

    >>> doble_impar(14)
    'la mitad del numero 14 ingresado es un numero impar'

    >>> doble_impar(12)
    'la mitad del numero 12 ingresado no es un numero impar'

    >>> doble_impar(0)
    'la mitad del numero 0 ingresado no es un numero impar'

    >>> doble_impar('hola')
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero o otro tipo de caracter

    >>> doble_impar(6.2)
    Traceback (most recent call last):
    ..
    TypeError: 6.2 no es un numero o otro tipo de caracter

    :param numero: El numero ingresado
    :return: Mensaje de validaciòn de si el nùmero ingresado es el doble de un nùmero impar
    """
    if int != type(numero):
        raise TypeError(str(numero) + ' no es un numero o otro tipo de caracter')

    elif ((numero/2) % 2 == 0):
        return ('la mitad del numero '+ str(numero) +' ingresado no es un numero impar')

    else:
        return ('la mitad del numero '+ str(numero) +' ingresado es un numero impar')

def comparar_cuadrado(numero1,numero2):
    """

    int, int -> str

    Compara si numero 2 es el cuadrado del numero 1; y si numero 2 es mayor o menor que el cuadrado del numero 1

    >>> comparar_cuadrado(2,4)
    'El segundo es el cuadrado del primero'

    >>> comparar_cuadrado(2,3)
    'El segundo es menor que el cuadrado del primero'

    >>> comparar_cuadrado(2,5)
    'El segundo es mayor que el cuadrado del primero'

    >>> comparar_cuadrado('hola', 5)
    Traceback (most recent call last):
    ..
    TypeError: Alguno de los dos numeros ingresados no es un numero o otro tipo de caracter

    >>> comparar_cuadrado(6.2, 6)
    Traceback (most recent call last):
    ..
    TypeError: Alguno de los dos numeros ingresados no es un numero o otro tipo de caracter

    :param numero1: Un numero entero
    :param numero2: Un posible numero entero
    :return: Un mensaje con la verificaciòn de si numero 2 es el cuadrado del numero 1; y si numero 2 es mayor o menor que el cuadrado del numero 1
    """

    if int != type(numero1) or int != type(numero2):
        raise TypeError('Alguno de los dos numeros ingresados no es un numero o otro tipo de caracter')
    elif ((numero1*numero1)== numero2):
        return ('El segundo es el cuadrado del primero')
    elif (numero1*numero1)> numero2:
        return ('El segundo es menor que el cuadrado del primero')
    elif (numero1*numero1)< numero2:
        return ('El segundo es mayor que el cuadrado del primero')

def numero_primo(numero):
    """
    int -> str

    Verifica si el nùmero ingresado es nùmero o no

    >>> numero_primo(2)
    '2 Es un numero primo'

    >>> numero_primo(4)
    '4 No es un numero primo'

    >>> numero_primo(0)


    >>> numero_primo()

    >>> doble_impar('hola')
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero o otro tipo de caracter

    >>> doble_impar(6.2)
    Traceback (most recent call last):
    ..
    TypeError: 6.2 no es un numero o otro tipo de caracter

    :param numero:
    :return:
    """

    if int != type(numero):
        raise TypeError(str(numero) + ' no es un numero o otro tipo de caracter')
    elif (((numero%numero)==0) == ((numero%1)==0))
        return (str(numero)+ ' Es un numero primo')
    else:
        return (str(numero)+ ' No es un numero primo')

def calcule_cantidad_billetes(cantidad):
   """
   num-> str

   Calcula la cantidad de billetes para una cantidad dada

   >>> calcule_cantidad_billetes(3300)
   ('Usted requiere 6 billetes de 500 y le sobra 300,Usted requiere 1 billetes de 200 y le sobra 300,Usted requiere 1 billetes de 100 y le sobra 100,', 'y le sobra ', 0)


   :param cantidad:
   :return: mensaje
   """
   ent=cantidad//500
   sobrante=cantidad%500
   if ent:
       mensaje =('Usted requiere '+ str(ent)+ ' billetes de 500 y le sobra '+ str(sobrante)+"," )

   ent=sobrante//200
   if ent:
       mensaje +=('Usted requiere '+ str(ent)+ ' billetes de 200 y le sobra '+ str(sobrante)+",")
   sobrante= sobrante%200
   ent=sobrante//100
   if ent:
       mensaje +=('Usted requiere '+ str(ent)+ ' billetes de 100 y le sobra '+ str(sobrante)+",")
   sobrante = sobrante % 100
   ent = sobrante // 50
   if ent:
       mensaje +=('Usted requiere ' + str(ent) + ' billetes de 50 y le sobra '+ str(sobrante)+",")
   sobrante = sobrante % 50
   ent = sobrante // 20
   if ent:
       mensaje +=('Usted requiere ' + str(ent) + ' billetes de 20 y le sobra '+ str(sobrante)+",")
   sobrante = sobrante % 20
   ent = sobrante // 10
   if ent:
       mensaje +=('Usted requiere ' + str(ent) + ' billetes de 10 y le sobra '+ str(sobrante)+",")

   sobrante = sobrante % 10
   return mensaje , 'y le sobra ' , sobrante

