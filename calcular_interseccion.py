def calcular_interseccion(conjunto1, conjunto2):
    interseccion = []
    
    for elemento_i in conjunto1:
        if elemento_i in conjunto2 and elemento_i not in interseccion:
            interseccion.append(elemento_i)
    return sorted(interseccion)

conjunto1 = [1, 2, 3, 4, 5, 6]
conjunto2 = [1, 3, 5, 7, 3, 9]

print(calcular_interseccion(conjunto1, conjunto2))
