# Ejercicio 1
def dividir_estudiantes():
    numero_estudiantes = 1
    lista_aprobados = []
    lista_reprobados = []


    while numero_estudiantes <= 10:
        nombre_estudiante = input('Nombre y apellido: ')
        calificacion_estudiante = int(input('Nota sobre 100pts: '))

        if calificacion_estudiante >= 51:
            lista_aprobados.append([numero_estudiantes, nombre_estudiante, calificacion_estudiante])
        else:
            lista_reprobados.append([numero_estudiantes, nombre_estudiante, calificacion_estudiante])
        numero_estudiantes += 1

    print('\nEstudiantes Aprobados: ')
    for aprobado in lista_aprobados:
        print(aprobado)


    print('\nEstudiantes Reprobados: ')
    for reprobado in lista_reprobados:
        print(reprobado)


# Ejercicio 2
def secuencia():
    sumatoria = 0
    numerador = 1
    denominador = 11
    impar = 1

    for i in range(1, 11):
        sumatoria = sumatoria + (numerador / denominador)

        # 1/4 + 4/12 + 9/13 ... + 100/20
        print(f"{numerador}/{denominador}", end=' + ')
        impar += 2

        numerador += impar
        denominador += 1
    print(f'\nEl resultado de la sumatoria es: {sumatoria}')
