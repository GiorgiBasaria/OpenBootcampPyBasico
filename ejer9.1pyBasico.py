
from functools import reduce

# Definimos una función que obtiene los elementos impares de una lista y los suma

def suma_impares(lista):
    impares = filter(lambda x: x % 2 != 0, lista) # Obtenemos los elementos impares con filter
    suma = reduce(lambda x, y: x + y, impares) # sumamos los emementos imapres con reduce
    return suma

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = suma_impares(lista)
print(suma) #Deberia imprimir 25, que es la suma de los impares de la lista (1 + 3 + 5 + 7 + 9)