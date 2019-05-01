# def analizar_hv(perfil,competencias):


ingredientes=[]
while ingredientes:
    pizza = input("Ingrese los ingredientes de su pizza")
    if pizza== 'pare':
        break
    ingredientes.append(pizza)
print ("Sus ingredientes son: ", ingredientes)