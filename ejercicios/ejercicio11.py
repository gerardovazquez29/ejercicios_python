# Crea una función que reciba una lista de números y devuelva la suma total.

def suma_lista(lista_numeros):
    total = 0
    for numeros in lista_numeros:
        total += numeros
    return total
resultado = suma_lista([2,6,4,8,7])
print(resultado)

print("-" * 20)

# Escribe una función que reciba una palabra y devuelva si es palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
resultado = es_palindromo("Reconocer")
print(resultado)

print("-" * 20)

# Crea una función que reciba 3 números y devuelva el mayor.
def num_mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(num_mayor(5,3,7))

print("-" *20) 

# Crea una función que reciba un texto y lo devuelva en mayúsculas.
def texto_mayusculas(texto):
    texto = texto.upper()
    return texto
texto = input("Escribe un texto y lo convierto en mayusculas: ")
print(texto_mayusculas(texto))

print("-" *20)

# Usa *args para crear una función que reciba cualquier cantidad 
# de números y devuelva su promedio.

def calcular_promedio(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    promedio = suma / cantidad
    return promedio
print(calcular_promedio(5,0,9,5))

print("-" *20)

