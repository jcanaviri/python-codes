def leer_calificaciones(ruta_archivo, codigo_asignatura):
    """leer_calificaciones retorna una lista con los estudiantes con notas validas"""
    lista_resultado = []

    # Abrimos el archivo
    with open(ruta_archivo) as archivo:
        # Leemos cada una de las lineas
        for linea in archivo.readlines():
            # El archivo contine la separacion de | en cada linea
            linea_separada = linea.split("|")

            # Como se indico el orden es carnet, materia, primer parcial, segundo parcial, final
            # en caso de los parciales se hace una conversion a flotante
            carnet = linea_separada[0]
            materia = linea_separada[1]
            primer_parcial = float(linea_separada[2])
            segundo_parcial = float(linea_separada[3])
            final = float(linea_separada[4])

            # Si el codigo es el que buscamos lo tomamos en cuenta
            if materia == codigo_asignatura:
                # La validacion es si la nota no esta en el rango de 0 a 100 no es una nota valida
                # en ese caso esquivamos la iteracion y continuamos en la siguiente
                if primer_parcial < 0 or primer_parcial > 100:
                    continue
                if segundo_parcial < 0 or segundo_parcial > 100:
                    continue
                if final < 0 or final > 100:
                    continue

                lista_resultado.append(
                    [carnet, materia, primer_parcial, segundo_parcial, final]
                )

    if len(lista_resultado) == 0:
        return None

    return lista_resultado


# print(leer_calificaciones('./notas.data', 'MAT103'))


def limpiar_calificaciones(calificaciones):
    """limpiar_calificaciones retorna una lista con los estudiantes con notas validas"""
    lista_resultado = []

    # Recorremos la lista de calificaciones
    for fila in calificaciones:
        carnet = fila[0]
        materia = fila[1]
        primer_parcial = float(fila[2])
        segundo_parcial = float(fila[3])
        final = float(fila[4])

        # Validamos que las notas esten en el rango de 0 a 100
        if primer_parcial < 0 or primer_parcial > 100:
            continue
        if segundo_parcial < 0 or segundo_parcial > 100:
            continue
        if final < 0 or final > 100:
            continue

        # Si todo esta correcto lo agregamos a la lista
        lista_resultado.append(
            [carnet, materia, primer_parcial, segundo_parcial, final]
        )

    # Si la lista no se agrego ningun elemento retornamos None
    if len(lista_resultado) == 0:
        return None

    return lista_resultado


calificaciones = [
    ["CU-749", "MAT204", 116.07, 50.71, 138.58],
    ["CU-1152", "MAT101", 37.93, 36.45, 136.64],
    ["CU-1374", "MAT103", 14.33, 54.81, 55.35],
    ["CU-332", "MAT101", 22.42, 119.29, 91.83],
]

# print(limpiar_calificaciones(calificaciones))


def calcular_calificacion_total(calificacion):
    """calcular_calificacion_total recibe una lista con los datos de un alumno y retorna
    la calificación del estudiante promediada por 30% 1er parcial, 30% 2do parcial y 40% el final"""
    primer_parcial = float(calificacion[2])
    segundo_parcial = float(calificacion[3])
    final = float(calificacion[4])

    calificacion_total = (
        (primer_parcial * 0.3) + (segundo_parcial * 0.3) + (final * 0.4)
    )
    return round(calificacion_total, 2)


calificacion = ["CU-1374", "MAT103", 14.33, 54.81, 55.35]
# print(calcular_calificacion_total(calificacion))


def a(b):
    c = None
    while c == None:
        try:
            c = input(b).upper()
            if len(c) < 6:
                print("Error")
                c = None
        except:
            print("Error")
    return c


codigo_asignatura = a("Ingrese la materia: ")
lista_calificaciones = leer_calificaciones("./notas.data", codigo_asignatura)
lista_limpia = limpiar_calificaciones(lista_calificaciones)

for alumno in lista_limpia:
    print(alumno, end=" ")
    print(f"calificacion final: {calcular_calificacion_total(alumno)}")
