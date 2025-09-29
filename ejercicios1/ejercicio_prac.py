# Ejercicios propuestos (sin solución)

# 1-Crea una función que reciba dos números y devuelva cuál es mayor.
def num_mayor(num1,num2):
    if num1 > num2 :
        mayor = num1
    elif num2 > num1:
        mayor = num2
    else:
        mayor = "son iguales"
    return print(f"el numero mayor es:{mayor}")
num_mayor(5,7) # el numero mayor es:7
            
# 2-Crea una función que calcule el área de un círculo (usa π ≈ 3.1416).
def area_circulo(radio):
    return 3.1416 * radio **2
radio = 6
area = area_circulo(radio)
print(f"El area del circulo con radio {radio} es: {area:.2f}")
  #  El area del circulo con radio 6 es: 113.10


# 3-Escribe una función que reciba un número y diga si es primo o no.
def num_primo(num):
    """ if num > 2 :
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False """
    for i in range(3, int(num**0.5) + 1,2):
        if num % i == 0:
            return False
    return True
print(num_primo(7)) # True

# 4-Crea una función que reciba una lista de números y devuelva la suma de los 
# pares.
#list_numeros = [1,2,3,4,5,6,7,8,9]
def sum_num_pares(numeros):
        suma = 0
        for num in numeros:
            if num % 2 == 0:
                suma += num
        return suma
lista = [1,2,3,4,5,6,7,8,9]
print(sum_num_pares(lista)) # 20

def suma_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)

lista = [9,8,7,4,5,6,3,2,4,5,6,9,8,7]
print(suma_pares(lista)) # 38   

# 5-Haz una función que reciba un texto y devuelva cuántas vocales tiene.
def texto_vocal(texto):
    vocales = "a,e,i,o,u,A,E,I,O,U,"
    contador = 0
    for letras in texto:
        if letras in vocales:
            contador += 1
    return contador
print(texto_vocal("FUNCION")) # 3
        
# 6-Usa *args para hacer una función que calcule el promedio de cualquier 
# cantidad de números.
def prom_num(*args):
    return  sum(args) / len(args)
print(prom_num(2,3,5,6,8,9)) # 5.5


# 7-Usa **kwargs para crear una función que muestre la información de una persona 
# (nombre, edad, ciudad, etc.).
def info_person(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
info_person(nombre='Ana', edad=22, ciudad='Guadalajara')

""" 
nombre = Ana
edad = 22
ciudad = Guadalajara 
"""
