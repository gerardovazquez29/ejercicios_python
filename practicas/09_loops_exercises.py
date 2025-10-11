# 1. Usa un bucle while para imprimir los números del 1 al 10.
numero = 1
while numero <= 10:
    print(numero)
    numero += 1  # 12345678910

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] 
# e imprime cada número.
lista = [10, 20, 30, 40, 50]
for n in lista:
    print(n)# 10,20,30,40,50

# 3. Escribe un programa que use un bucle while para sumar los números 
# del 1 al 100 e imprime el resultado.
suma = 0
num = 1
while num <= 100:
    suma += num
    num += 1
print(f'la suma de los numeros del 1 al 100 es: {suma}')
# la suma de los numeros del 1 al 100 es: 5050


# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
cadena = "Python"
for caracter in cadena:
    print(caracter)# python

# 5. Usa un bucle while para encontrar el primer número 
# divisible por 7 entre 1 y 50.
divisible = []
numeros = 1
while numeros <= 50:
    if numeros % 7 == 0:
        divisible = numeros
        break
    numeros += 1
print(divisible) # 7

# 6. Usa un bucle for para recorrer el diccionario 
# {"name": "Brais", "age": 37, "country": "Galicia"} 
# e imprime las claves.
dic = {"name": "Brais", "age": 37, "country": "Galicia"}
for claves in dic.keys():
    print(claves) # name, age, country

# 7. Escribe un programa que use un bucle while para imprimir 
# los números pares entre 1 y 20.
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n += 1
# 2,4,6,8,10,12,14,16,18,20

# 8. Usa un bucle for con la función range() para imprimir los números 
# del 1 al 10 en orden inverso.
for n in range(10,0,-1):
    print(n) # 10,9,8,7,6,5,4,3,2,1

# 9. Escribe un programa que use un bucle for para contar cuántas veces 
# aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
lista = [30, 10, 30, 20, 30, 40]
contador = 0
for n in lista:
    if n == 30:
        contador += 1
print(f'El numero 30 aparese {contador} veses')
# El numero 30 aparese 3 veses


# 10. Usa un bucle for para recorrer una lista de nombres y detener 
# el bucle cuando se encuentre el nombre "Brais".
nombres = ['luis','pedro', 'jorge', 'santiago','brais','gerardo','jose']
contando = 0

for nom in nombres:
    if nom == 'brais':
        contando = nom
        break
    contando += 1
print(contando)

