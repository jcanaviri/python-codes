def calcular_es_subconjunto(conjunto1, conjunto2):
    """Funcion que returnara un valor booleano Verdadero si un conjunto es subconjunto
    del otro y Falso en caso contrario"""

    # Calculamos cual es el conjunto más pequeño
    if len(conjunto1) <= len(conjunto2):
        # Si la condicion es verdadera significa que conjunto1 es el menor
        for elemento_i in conjunto1:
            # Si el elemento no es parte del otro conjunto significa que no es un subconjunto
            if elemento_i not in conjunto2:
                return False
        return True
    else:
        # Si la condicion es falsa significa que conjunto2 es el menor
        for elemento_j in conjunto2:
            # Si el elemento no es parte del otro conjunto significa que no es un subconjunto
            if elemento_j not in conjunto1:
                return False
        return True


conjunto1 = [1, 2, 3]
conjunto2 = [4, 5, 6]

print(calcular_es_subconjunto(conjunto1, conjunto2))  # False

conjunto1 = [1, 2, 3]
conjunto2 = [4, 5, 6, 1, 2, 3]

print(calcular_es_subconjunto(conjunto1, conjunto2))  # True

conjunto1 = [1, 2, 3, 4, 5, 6]
conjunto2 = [4, 5, 6]

print(calcular_es_subconjunto(conjunto1, conjunto2))  # True
