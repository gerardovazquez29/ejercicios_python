
# Escribe un programa que imprima los números del 100 al 1, de 10 en 10.
#for i in range(1, 100):
#    print(i)


# Crea una lista de números del 1 al 50 y muestra solo los múltiplos de 5.
"""

lista = []
for numeros in range(1,51):
    if numeros % 5 == 0:
        lista.append(numeros)
print(lista)
"""
# Pide al usuario que ingrese palabras hasta que escriba "salir", luego 
# imprime todas las palabras escritas.
"""

lista_palabras = []
while True:
    palabras = input("ingresa las palabras que quieras hasta que escribas 'salir'").lower()
    if palabras == 'salir':
        break
    lista_palabras.append(palabras)
print(lista_palabras)
"""
# Recorre una cadena e imprime cuántas veces aparece cada letra (usa un diccionario).

diccionario = {}
palabra = str(input('Escribe unas palabras: ')).lower()
for letra in palabra:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1
print(diccionario)

# Usa dos bucles anidados para imprimir un rectángulo de # de 4 filas y 10 columnas.
for fila in range(4):
    for columna in range(10):
        print("#", end="" )
    print()
print()
