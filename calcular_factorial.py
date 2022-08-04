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
    return numero * calcular_factorial(numero-1)

print(calcular_factorial(5))  # 120
