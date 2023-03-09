#####################
#   EJERCICIO - 1   #
#####################
def leer_puntos(ruta_archivo):
    """Esta funcion lee el archivo y retorna una lista con puntos validos"""
    puntos_validos = []

    with open(ruta_archivo) as archivo:  # Abrimos el archivo
        for linea in archivo.readlines():
            linea_separada = linea.split("#")

            # Si contiene cuatro elementos podemos validar si es correcto
            if len(linea_separada) == 4:
                codigo = linea_separada[0]
                nombre = linea_separada[1]
                coordenada_x = float(linea_separada[2])
                coordenada_y = float(linea_separada[3])

                # Validamos los tipos
                if all(
                    [
                        isinstance(codigo, str),
                        isinstance(nombre, str),
                        isinstance(coordenada_x, float),
                        isinstance(coordenada_y, float),
                    ]
                ):
                    punto_valido = [codigo, nombre, coordenada_x, coordenada_y]
                    puntos_validos.append(punto_valido)

    # Si la lista estaria vacia retornamos None
    if puntos_validos != []:
        return puntos_validos
    return None


# print(leer_puntos("./puntos.data"))


#####################
#   EJERCICIO - 2   #
#####################
def filtrar_puntos(puntos, origen, distancia):
    """Filtra la lista de puntos que esten dentro de un cuadrado"""
    lista_limpia = []
    for punto in puntos:
        coordenada_x = punto[2]
        coordenada_y = punto[3]

        # Calculamos la distancia entre la coordenada y el origen tango x como y
        distancia_x = coordenada_x - origen[0]
        distancia_y = coordenada_y - origen[1]

        # Si la distancia obtenida esta en los límites del cuadrado
        if (
            distancia_x > origen[0]
            and distancia_x < (distancia_x + distancia)
            and distancia_y > origen[1]
            and distancia_y < (distancia_y + distancia)
        ):
            lista_limpia.append(punto)

    # Si la lista estaria vacia retornamos None
    if len(lista_limpia) > 0:
        return lista_limpia
    return None


puntos = leer_puntos("./puntos.data")
origen = [0, 0]
distancia = 5
# print(filtrar_puntos(puntos, origen, distancia))


#####################
#   EJERCICIO - 3   #
#####################
def obtener_fuera_interseccion(region1, region2):
    """Retorna los elementos fuera de la interseccion de las regiones"""
    lista_interseccion = []

    for punto in region1:
        # Si pertenece a region1 y no a region2
        if punto in region1 and not punto in region2:
            lista_interseccion.append(punto)

    for punto in region2:
        # Si pertenece a region2 y no a region1
        if punto in region2 and not punto in region1:
            lista_interseccion.append(punto)

    # Si la lista estaria vacia retornamos None
    if lista_interseccion != 0:
        return lista_interseccion
    return None


puntos = leer_puntos("./puntos.data")
origen1 = [0, 0]
origen2 = [3, 3]
distancia = 10

region1 = filtrar_puntos(puntos, origen1, distancia)
region2 = filtrar_puntos(puntos, origen2, distancia)
# print(obtener_fuera_interseccion(region1, region2))


#####################
#   EJERCICIO - 4   #
#####################
# Leemos todos los puntos del archivo
puntos = leer_puntos("./puntos.data")

# Origenes y distancia
origen1 = [0, 0]
origen2 = [3, 3]
distancia = 10

# Obtenemos las regiones correctas
region1 = filtrar_puntos(puntos, origen1, distancia)
region2 = filtrar_puntos(puntos, origen2, distancia)

# Obtenemos los elementos que son no comunes con obtener_fuera_interseccion
elementos_no_comunes = obtener_fuera_interseccion(region1, region2)

# Creamos el archivo no_comunes.data e insertamos los no comunes
with open("./no_comunes.data", mode="w") as archivo:
    for elemento in elementos_no_comunes:
        cadena = (
            elemento[0]
            + "#"
            + elemento[1]
            + "#"
            + str(elemento[2])
            + "#"
            + str(elemento[3])
            + "\n"
        )
        archivo.write(cadena)
