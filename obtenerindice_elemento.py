def obtenerindice_elemento(lista_letras, letra):
    # lista_indices almacenara los indices donde aparezca el parametro letra
    lista_indices = []
    for indice, letra_actual in enumerate(lista_letras):
        # Si es la letra que buscamos la agregamos a la lista
        if letra_actual == letra:
            lista_indices.append(indice)

    # SI no tiene elementos es decir si la letra no aparecee
    # debe retornar None
    if len(lista_indices) > 0:
        return lista_indices
    else:
        return None

lista_letras = ['p', 'w', 'm', 'p']
letra = 'p'

print(obtenerindice_elemento(lista_letras, letra))
