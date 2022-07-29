def count_element(lista_numeros, numero):
    # Declaramos la variable veces que almacenara el número de veces 
    # que numero aparece en lista_numeros
    veces = 0
    
    for num in lista_numeros:
        # Si es el numero que buscamos veces incrementa
        if num == numero:
            veces += 1

    # Si no existe ese numero retornamos None
    # pero si existe lo retornamos
    if veces == 0:
        return None
    else:
        return veces

lista_numeros = [1, 2, 3, 2, 5]
numero = 9

print(count_element(lista_numeros, numero))
