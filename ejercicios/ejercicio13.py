
lista = [(3, 2), (1, 5), (4, 1)]
ordenada = sorted(lista, key=lambda x: x[0])
print(ordenada)  # [(1, 5), (3, 2), (4, 1)]

print('-' *20)

numeros = [1, 2, 3, 4, 5, 6, 25,28,36]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 28, 36]

print('-'*20)

#  Crea una función que reciba cualquier 
# cantidad de números con *args y devuelva el promedio. 
# Consejo: Usa sum() y len() sobre args.
def promedio(*numeros):
    if len(numeros) == 0:
        return 0
    suma = sum(numeros)
    cantidad = len(numeros)
    return suma / cantidad
print(promedio(4,9,7)) # = 6.666666666666667

print('-' *20)

# obtener los cuadrados de los números pares
numeros = [1,2,3,4,5,6]
cuadrado_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrado_pares) # = [4, 16, 36]

print('-' *20)

# convertir palabras a mayúsculas
palabras = ['perro','loro','cantar']
mayusculas = [p.upper() for p in palabras]
print(mayusculas) # = ['PERRO', 'LORO', 'CANTAR']

print('-' *20)

# : crear un diccionario con número:cuadrado
numeros = [2,6,7,9]
dic_cuadrados = {n: n ** 2 for n in numeros}
print(dic_cuadrados) # = {2: 4, 6: 36, 7: 49, 9: 81}

print('-' *20)

