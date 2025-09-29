"""
Ejercicio 1 
    - Crear variables una 'pais' y otra 'continente'
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""
pais = "Mexico"
continente = "America"

print(pais) # <class 'str'>   Mexico
print(continente) #<class 'str'>  America

print('-' *30)
"""
Ejercicio 2
    - Escribir un script que nos muestre por pantalla todos 
      los numeros pares del 1 al 120
"""
for pares in range(1, 121):
    if pares % 2 == 0:
        print(pares)
# 2,4,6,8,10,12,-,-,-,120

print('-'*30)

"""
Ejercicio3
    - Escribir un programa que muestre los cuadrados
      (un numero multiplicado por si mismo) de los 60 
      primeros numeros naturales. Resolverlo con los
      bucles for y while  
"""

for i in range(1,61):
    cuadrado = i ** 2
    print(f"El Cuadrado de {i} es {cuadrado}")

print('-'*30)

# Solución con bucle while
numeros = 1
while numeros <= 60:
    cuadrado = numeros ** 2
    print(f"el cuadrado de {numeros} es {cuadrado}")
    numeros += 1  
    # Importante: incrementar la variable para evitar ciclo infinito

print('-'*30)

"""
Ejercicio4
    - Pedir dos numeros al usuario y hacer todas las operaciones basicas  
      de una calculadora y mostrarlo por pantalla

"""

numero1 = int(input('ingresa el primer numero: '))
numero2 = int(input('ingresa el segundo numero: '))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    divicion = numero1 / numero2
    modulo = numero1 % numero2
else:
    divicion = "No se puede dividir entre 0"
    modulo = "No se puede obtener modulo con 0"

print("\n Resultados")
print(f"La Suma de los numeros {numero1} y {numero2} = {suma}")
print(f"La Resta de los numeros {numero1} y {numero2} = {resta}")
print(f"La multiplicacion de los numeros {numero1} y {numero2} = {multiplicacion}")
print(f"La Division de los numeros {numero1} y {numero2} = {divicion}")
print(f"El Modulo de los numeros {numero1} y {numero2} = {modulo}")

