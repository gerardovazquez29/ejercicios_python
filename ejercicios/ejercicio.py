"""
Ejercicio7
    - Hacer un programa que muestre todos los numeros 
      impares entre dos numeros que decida el usuario.    
"""
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

# Asegurar que numero1 sea menor que numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"\n Numeros impares entre {numero1} y {numero2}: ")

impares_encontrados = []

for numero in range(numero1,numero2 + 1):
    if numero % 2 != 0:
        impares_encontrados.append(numero)

if impares_encontrados:
    print("Los numeros impares son; ")
    for impar in impares_encontrados:
        print(impar, end=" ")
    print()
    print(f"Total de numeros impares encontrados son: {len(impares_encontrados)}")
else:
    print("No se encontraron numeros impares en el rango especificado")

