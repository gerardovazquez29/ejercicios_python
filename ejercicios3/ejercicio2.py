
contador = 0
while contador <= 11:
    print(f"Contador: {contador}")
    contador += 1

frutas = ['manzana', 'banana', 'pera']
for fruta in frutas:
    print(f"fruta: {fruta}")

# Iterar usando range()
for numero in range(1, 6):  # Del 1 al 5
    print("Número:", numero)


for i in range(3):
    print(i)
else:
    print("El bucle terminó normalmente.")

nombres = ["Ana", "Luis", "Carlos"]
for i, nombre in enumerate(nombres):
    print(f"Índice: {i}, Nombre: {nombre}")

nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años") # Ana tiene 25 Años

# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)   # [1,4,9,16,25]

# Filtrar números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares) # [0,2,4,6,8]


# Imprimir una matriz
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ') # imprime un espacio en blanco
    print()  # salto de linea

# Bucle hasta que el usuario escriba "salir"
while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    if entrada == "salir":
        break
    print("Escribiste:", entrada)

# Triángulo de asteriscos
for i in range(1, 6):
    print("*" * i)
