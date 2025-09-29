def saludar(nombre):
    print(f'Hola, {nombre}! ¿Cómo estás?')

saludar('Juan')
saludar('María')

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Imprime [2, 4, 6, 8, 10]


def es_par(numeros):
    return numeros % 2 == 0
print(es_par(8))
print(es_par(7))

