# letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numeros = "01234566789"
# simbolos = "!@#$%^&*()_+-=[]{}\;:,.<>?/"
# caracteres = letras + numeros + simbolos
# formula simple: (item * 7 + 3) % len(caracteres)

# entrada: 8
# salida: &D^#23SN

import string
import random

def pasword_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    for item in range(length):
        index = random.choice(chars)
        password.append(index)

    return ''.join(password)

length = int(input("¿Cuantos caracteres quieres en tu contraseña? "))
print("Tu contraseña segura es:", pasword_generator(length))