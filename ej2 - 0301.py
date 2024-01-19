import csv
import cProfile

letras = ["T", "R", "W", "A","G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

def leer_fichero(fichero):
    
    """Función que lee los ficheros con una lista larga de datos de personas, en este caso 50 y 1000, y llama a 2 funciones,
      una que calcula la letra del dni y otra que escribe los nombres en formato capitalizado
Parámetros:
- fichero: La variable que utilizamos para nombrar a los ficheros que queramos leer
Salida:
Muestra por pantalla los nombres capitalizados, los números de los dni y por último su letra ya calculada 
"""
    with open(fichero, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        lista = list(csv_reader)
        for linea in lista:
            nombre = linea[0]
            dni = linea[1]
            letra_dni = calcular_letra_dni(dni)
            nombres = nombre_capitalizado(nombre)
            print(nombres + "  " + dni + "  " + "Su letra del DNI es: " + letra_dni)

def calcular_letra_dni(dni):
        
    """Función que calcula la letra del dni a través de una fórmula
Parámetros:
- dni: La variable que contendrá los números de los dni
Salida:
Cálculo de la letra del dni.
"""
    return letras[int(dni) % 23]
        
def nombre_capitalizado(nombre):
    
    """Función que recibe nombres y los devuelve en formato capitalizado
Parámetros:
- nombre: La variable que contendrá diferentes nombres
Salida:
Los nombres en formato capitalizado.
"""
    return nombre.title()
    
leer_fichero("50.csv")
leer_fichero("1000.csv")

cProfile.run('leer_fichero("50.csv")')
cProfile.run('leer_fichero("1000.csv")')