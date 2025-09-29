# Funciones + Condicionales

# -Escribe una función es_par(n) que reciba un número y 
#  devuelva True si es par y False si es impar.
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(es_par(18)) # True

# -Escribe una función clasificar_edad(edad) que regrese 
#  "Niño", "Joven", "Adulto", "Mayor" según la edad.
def clasificar_edad(edad):
    if edad >= 25:
        return "Adulto"
    elif edad >= 65:
        return "Mayor"
    elif edad >= 18:
        return "Joven"
    else:
        return "Niño"
edad = 23
print(clasificar_edad(edad)) # Joven

# Funciones + Bucles
 
# -Crea una función suma_lista(lista) que reciba una lista de números 
#  y devuelva la suma de todos ellos.
def suma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total
lista = [8,4,6,8,7,2]
print(suma_lista(lista)) # 35

# -Escribe una función contar_vocales(texto) que reciba un string y 
#  devuelva cuántas vocales tiene.
def contar_vocales(texto):
    vocales = "a,e,i,o,u,A,E,I,O,U"
    contador = 0
    for letras in texto:
        if letras in vocales:
            contador += 1
    return contador
print(contar_vocales("PRIMERA")) # 3




# Funciones + Listas
 
# -Crea una función invertir_lista(lista) que regrese una 
#  lista al revés sin usar .reverse().
def invertir_lista(lista):
    return lista[::-1]
lista = [1,2,3,4,5,6]
print(invertir_lista(lista)) # [6, 5, 4, 3, 2, 1]

# -Define una función duplicar_numeros(lista) que devuelva 
#  una nueva lista con cada número multiplicado por 2.
def duplicar_numeros(lista):
    lista_multiplicada = []
    for num in lista:
        numero = num * 2
        lista_multiplicada.append(numero)
    return lista_multiplicada
lista = [5,7,3]
print(duplicar_numeros(lista)) # [10, 14, 6]

# Funciones + Tuplas
 
# -Crea una función max_min(tupla) que reciba una tupla 
#  de números y regrese el valor máximo y mínimo.
def max_min(tupla):
    maximo = max(tupla)
    minimo = min(tupla)
    return maximo, minimo
tupla = (2,9,7,3,6)
print(max_min(tupla)) # (9, 2)

# -Escribe una función buscar_elemento(tupla, valor) que 
#  indique si el elemento está dentro de la tupla.
def buscar_elemento(tupla, valor):
    
    return valor in tupla
tupla = (2,5,9,7,8)
print(buscar_elemento(tupla,9))# True

# Funciones + Diccionarios


# -Define una función contar_palabras(texto) que regrese 
#  un diccionario con las palabras como claves y el número 
#  de repeticiones como valores.
def contar_palabras(texto):
    texto = texto.lower()
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
texto = "Hola mundo dev hola python Dev hola todos "
resultado = contar_palabras(texto)
print(resultado)
 # {'hola': 3, 'mundo': 1, 'dev': 2, 'python': 1, 'todos': 1}

def contar_palabra(texto):
    contador = {}
    for palabra in texto.lower().split():
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador
texto = "Hola mundo dev hola python Dev hola todos "
resultado = contar_palabras(texto)
print(resultado)


# -Crea una función agregar_contacto(diccionario, nombre, telefono) 
#  que agregue un contacto a un diccionario de teléfonos.
def agregar_contacto(diccionario, nombre, telefono):
    diccionario[nombre] = telefono
    return diccionario
agenda = {}
print(agregar_contacto(agenda,"Gerardo",554456325))
   # {'Gerardo': 554456325}

# Funciones + Sets


# -Crea una función union_sets(set1, set2) que devuelva la unión 
#  de dos conjuntos.
def union_sets(set1, set2):
    union = set1 | set2
    return union
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
print(union_sets(set1,set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# -Haz una función elementos_unicos(lista) que tome una lista y 
#  devuelva los elementos únicos usando un set.
def elementos_unicos(lista):
    lista_unica = set(lista)
    return lista_unica
lista = [1,2,3,4,5,6,5,2,3,6,1]
print(elementos_unicos(lista))
   # {1, 2, 3, 4, 5, 6}


def logger(func):
    def envoltura(*args, **kwargs):
        print(f"llamando {func.__name__} con {args} {kwargs}")
        resultado = func(*args, **kwargs)
        print(f" {func.__name__} devolvio {resultado}")
        return resultado
    return envoltura

@logger
def sumar(a,b): return a + b

# Ejemplo 1: Solo argumentos posicionales
print("=== Ejemplo 1: Argumentos posicionales ===")
sumar(4,6)

# Ejemplo 2: Con argumentos con nombre (kwargs)
print("\n=== Ejemplo 2: Argumentos con nombre ===")
sumar(a=4, b=6)

# Ejemplo 3: Mixto (posicionales y con nombre)
print("\n=== Ejemplo 3: Mixto ===")
sumar(4, b=6)
""" 
llamando sumar con (4, 6) {}
 sumar devolvio 10 
 """
