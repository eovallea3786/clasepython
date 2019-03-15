# def funcion (numero1,palabra,numero2):
#     """
#
#
#
#     :param numero1:
#     :param palabra:
#     :param numero2:
#     :return:
#
#
#     if numero1<=len(palabra):
#         return ()
#     else:
#         return False
#
#     """
#
# def ejerciciotry(numero):
#     """
#
#
#     :return:
#     """
#     try:
#         print('tu numero {0} al cuadrado es {1}'.format(numero,float(numero)**2))
#     except:
#         print('{0} no es un numero'.format(numero))

numero1=input("Ingrese primer numero ")
numero2=input("Ingrese segundo numero ")

try:
    print("la division de dos numeros {0}".format(float(numero1) / float(numero2)))
except:
    print("algo en la division esta mal")
