# 1. Crea una función llamada "personalized_greeting" que reciba un nombre 
# como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, 
# debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="desconocido"):
    return f"Hola {name}"
saludo = personalized_greeting()
print(saludo) # Hola desconocido

# 2. Escribe una función llamada "multiply" que reciba dos números como 
# argumentos y retorne el resultado de multiplicarlos.
def multiply(num1,num2):
    total = num1 * num2
    return f"El resultado de {num1} x {num2} = {total}"
print(multiply(5,6)) # El resultado de 5 x 6 = 30

# 3. Crea una función llamada "is_even" que reciba un número entero 
# como argumento y retorne True si es par y False si es impar.
def is_even(num):
    if num % 2  !=  0:
        return False
    return True
print(is_even(8)) # True

# 4. Escribe una función llamada "convert_to_uppercase" que reciba 
# una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(texto):
    return texto.upper()
print(convert_to_uppercase('python es genial'))  #PYTHON ES GENIAL

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario 
# de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*args):
    total = sum(args)
    return total
print(arbitrary_sum(2,8,3,9,7,8)) # 37

# 6. Escribe una función llamada "generate_full_greeting" que reciba 
# dos argumentos: nombre y apellido, y retorne el saludo 
# completo "Hola, <nombre> <apellido>". 
# Los argumentos deben ser pasados por clave.
def generate_full_greeting(**kgars):
    nombre = kgars.get('nombre' )
    apellido = kgars.get('apellido')
    return f"Hola {nombre} {apellido}"
print(generate_full_greeting(nombre="Gerardo", apellido="Vazquez"))
# Hola Gerardo Vazquez

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
