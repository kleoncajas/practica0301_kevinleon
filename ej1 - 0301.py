import datetime

def FiboRec(n):
    """Función que recibe un número entero positivo y calcula el número de fibonacci asociado a ese número de manera recursiva
Parámetros:
- n: La variable que contendrá un número entero positivo
Salida:
Número de fibonacci ya calculado
"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FiboRec(n-1) + FiboRec(n-2)

start_time = datetime.datetime.now()    
print(FiboRec(1))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)

def FiboBucle(n):
    """Función que recibe un número entero positivo y calcula el número de fibonacci asociado a ese número con bucles
Parámetros:
- n: La variable que contendrá un número entero positivo
Salida:
Número de fibonacci ya calculado
"""
    a = 0
    b = 1
    for i in range(n):
        c = b+a
        a=b
        b=c   
    return a

start_time = datetime.datetime.now()
print(FiboBucle(1))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)