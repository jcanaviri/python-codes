import math


def calcular_factorial(numero):
    """calcular_factorial recibe como parametro un numero entero y
    retorna el factorial de este numero"""

    # Si es negativo retornar None
    if numero < 0:
        return None

    # Si el numero es 0 su factorial es 1
    if numero == 0 or numero == 1:
        return 1

    # El factorial de un numero es el mismo numero multiplicado por todos los numeros anteriores a este
    # ejemplo el factorial de 5 es igual a 5 * 4 * 3 * 2 * 1 = 120
    return numero * calcular_factorial(numero - 1)


# calcular_factorial(5)  # 120


def calcular_seno(angulo, numero_terminos):
    """calcular_seno recibe como parametro un angulo expresado en radianes y
    retorna el seno de ese angulo"""

    lista_elementos = []  # almacenara los elementos de la sumatoria
    sumatoria = 0  # primer valor a cero

    # Signo varia de 1 a -1 y exponente crece en forma inpar es decir 1, 3, 5, ...
    signo = 1
    exponente = 1

    for _ in range(numero_terminos):
        termino_actual = (angulo**exponente / calcular_factorial(exponente)) * signo

        sumatoria += termino_actual
        lista_elementos.append(termino_actual)

        signo = signo * -1
        exponente += 2

    print(f"El seno calculado: {sumatoria}")  # 1.000000002
    print(f"El seno real: {math.sin(math.pi / 2)}")  # 1.0

    return lista_elementos


# calcular_seno(math.pi / 2, 50)


class MiError(Exception):
    pass


try:
    angulo = int(
        input("Ingrese el angulo expresado en grados sexagesimales (de 0° a 360°): ")
    )
    numero_terminos = int(input("Ingrese la cantidad de términos de la sumatoria: "))

    if angulo < 0 or angulo > 360:
        raise MiError(f"El angulo '{angulo}' no esta en el rango permitido")
    if numero_terminos <= 0:
        raise MiError(f"El numero de termino '{numero_terminos}' debe ser positivo")

    angulo_radianes = angulo * math.pi / 180
    lista_valores = calcular_seno(angulo_radianes, numero_terminos)

    with open("sumados.txt", "w") as archivo:
        for elemento in lista_valores:
            archivo.write(str(elemento) + "\n")

    print(lista_valores)
except ValueError:
    print("No ha ingresado datos de forma correcta")
except MiError as e:
    print(e)
