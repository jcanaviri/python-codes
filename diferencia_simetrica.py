# Defina una función que reciba dos listas y devuelva los elementos no comunes de ambas, sin repetir ninguno (diferencia simétrica de conjuntos).

# [5 Puntos] La función debe llamarse calcular_diferencia_simétrica.
# [5 Puntos] La función debe recibir los parámetros: conjunto1 y conjunto2.
# [5 Puntos] La función debe tener documentación.
# [30 Puntos] La función debe calcular los elementos no comunes de conjunto1 y conjunto2.
# [5 Puntos] La función debe devolver una lista sin elementos repetidos.


def calcular_diferencia_simetrica(conjunto1, conjunto2):
    """Creamos un módulo que devuelve los elementos no comunes de las listas
    recibidas como parámetros conjunto1 y conjunto2"""

    # Esta lista almacenara los elementos que no sean comunes
    # es decir la diferencia simetrica de tales conjuntos
    elementos_no_comunes = []

    # Iteramos sobre el conjunto1 y lo agregamos a la lista
    # solamente si el elemento1 no es parte del conjunto2
    for elemento1 in conjunto1:
        if elemento1 not in conjunto2:
            elementos_no_comunes.append(elemento1)

    # Iteramos sobre el conjunto2 y lo agregamos a la lista
    # solamente si el elemento2 no es parte del conjunto1
    for elemento2 in conjunto2:
        if elemento2 not in conjunto1:
            elementos_no_comunes.append(elemento2)

    # Finalmente la lista contentra la diferencia
    # simetrica asi que la retornamos
    return elementos_no_comunes


conjunto1 = [1, 2, 3]
conjunto2 = [1, 5, 3]

# La diferencia simetrica de los conjutos son los números 2 y 5 ya que
# no son parte del otro conjunto
print(calcular_diferencia_simetrica(conjunto1, conjunto2))  # [2, 5]


# Segundo Ejercicio

def obtener_indice_elemento(lista_nombres, nombre):
    """Esta funcion recibe como parametros lista_nombres y nombre
    retornara una lista con los indices en los que aparece el elemento en la lista"""
    # Lista que almacenara todas posiciones en las que aparece el parametro nombre
    posiciones = []

    # Verificamos si el elemento actual es nombre
    for indice, elemento in enumerate(lista_nombres):
        if elemento == nombre:
            posiciones.append(indice)

    # Si no existiese ninguna ocurrencia del nombre a buscar retornamos None
    if len(posiciones) == 0:
        return None

    # Caso contrario retornamos la lista de posiciones
    return posiciones

lista_nombres = ["John", "Dave", "Mary", "Susan", "Dave"]
print(obtener_indice_elemento(lista_nombres, "John")) # [0]
print(obtener_indice_elemento(lista_nombres, "Dave")) # [1, 4]
print(obtener_indice_elemento(lista_nombres, "Otro nombre que no esta en la lista")) # None
