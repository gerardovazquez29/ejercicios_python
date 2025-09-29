# 1. Crea una lista con los números del 1 al 5 e imprímela.
numeros = [1,2,3,4,5]
#*print(numeros)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista = [10, 20, 30, 40, 50]
#*print(lista[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
numeros=[1,2,3,4,5]
numeros.append(6)
#*print(numeros)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
numero = [10, 20, 30, 40, 50]
numero.insert(2, 15)
#*print(numero)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
lista1 = [10, 20, 30, 30, 40, 50]
lista1.remove(30)
#*print(lista1)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
lista = [1, 2, 3, 4, 5]
ultimo_elemento = lista.pop()
#*print(ultimo_elemento)
#*print(lista)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
lista= [100, 200, 300, 400, 500]
lista.reverse()
#*print(lista)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
lista = [3, 1, 4, 2, 5]
lista.sort()
#*print(lista)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
#*print(lista_concatenada)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
lista = [10, 20, 30, 40, 50]
sublista = lista[1:3]
print(sublista)
