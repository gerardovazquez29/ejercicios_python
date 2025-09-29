# Crea una función que reciba tu edad y diga si eres mayor de edad.
def saludo():
    edad = int(input("Dime cuantos años tienes: "))
    if edad >= 18:
        print(f"Tu Edad es: {edad} Eres mayor de edad")
    else:
        print(f"Tu Edad es: {edad} Eres menor de edad")
    return edad
saludo()

print("-" * 20)

# Escribe una función que reciba una cadena y devuelva cuántas letras tiene.
def contar_cadena():
    texto = input("Escribe una cadena de texto: ")
    cantidad = len(texto.replace(" ", ""))
    print(f"La cadena de texto: {texto} tiene: {cantidad} letras")
    return cantidad
contar_cadena() 


print("-" * 20)

# Escribe una función que multiplique dos números.
def multiplicar_num(a, b):
    numeros = a * b
    return numeros
print(multiplicar_num(6,7))

print("-" * 20)

# Crea una función que reciba un número y devuelva si es par o impar.
print("Hola Te gustaria saber si un numero es par o impar")
def par_o_impar():
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        print(f"El numero; {numero} es par")
    else:
        print(f"El numero: {numero} es impar")
    return numero
par_o_impar()

print("-" * 20)

# Escribe una función que reciba tu nombre y devuelva "Hola, [nombre]".
def nombre_saludo():
    nombre = input("Ingresa tu Nombre: ")
    print(f"Hola {nombre}")
nombre_saludo()
