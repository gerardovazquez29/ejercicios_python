# Escribe una función recursiva que calcule la suma de los 
# primeros n números naturales.

def suma_naturales(n):
    if n <= 1:
        return n
    else:
        return n + suma_naturales(n - 1)
    
print(suma_naturales(7))# 28
print(suma_naturales(3))# 6

print("-" *20)

# Usa una función lambda para ordenar una 
# lista de tuplas por el segundo valor.

lista = [(1,3),(2,4),(4,8),(6,7),(3,5)]
lista_ordenada = sorted(lista,key=lambda x:x[1])
print(lista_ordenada)
# = [(1, 3), (2, 4), (3, 5), (6, 7), (4, 8)]

print("-" * 20)

# Crea una función que reciba una función y un número, y 
# aplique esa función al número tres veces
def aplicar_trs_veces(funcion, numero):
    return funcion(funcion(funcion(numero)))
print(aplicar_trs_veces(lambda x: x + 1,4))
# = 7

print("-"* 20)

# Escribe una función que reciba una lista de números y 
# devuelva otra lista con los números al cuadrado (usa map).

def cuadrado(lista):
    return list(map(lambda x: x** 2, lista))
numeros = [2,3,5,6]
print(cuadrado(numeros))
# = [4,9,25,36]

print("-"*20)

# Usa **kwargs para mostrar 
# los datos de una persona (nombre, edad, ciudad, etc.).

def mostrar_datos_persona(**kwargs):
    print('Datos de la persona')
    for clave,valor in kwargs.items():
        print(f"-{clave.capitalize()}: {valor}")
mostrar_datos_persona(nombre="Gerardo",edad=44,ciudad='Tlaquepaque',ocupacion='Ingeniero')
"""
Datos de la persona
-Nombre: Gerardo
-Edad: 44
-Ciudad: Tlaquepaque
-Ocupacion: Ingeniero
"""
