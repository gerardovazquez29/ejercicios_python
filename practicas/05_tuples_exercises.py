# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

#*mi_tupla= (10, 20, 30, 40, 50)
#*print(type(mi_tupla))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
#*tupla = (100, 200, 300, 400, 500)
#*print(tupla[1]) #*200

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
#*tupla = (1, 2, 3)
#*tupla[0] = 10
#*print(tupla)  # Esto generará un error porque las tuplas son inmutables.

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
#*tupla = (1, 2, 3, 3, 4, 5, 3)
#*print(tupla.count(3)) #* 3

# 5. Encuentra el índice de la primera aparición de la cadena "Python" 
# en la tupla ("Java", "Python", "JavaScript", "Python").
#*tupla = ("Java", "Python", "JavaScript", "Python")
#*print(tupla.index("Python")) #* 1

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
#*tupla1 = (1, 2, 3)
#*tupla2 = (4, 5, 6)
#*tupla_concatenada = tupla1 + tupla2
#*print(tupla_concatenada)  #* (1, 2, 3, 4, 5, 6)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) 
# de la tupla (10, 20, 30, 40, 50).
#*tupla = (10, 20, 30, 40, 50)
#*subtupla = tupla[2:4]
#*print(subtupla)  #* (30, 40)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento 
# a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
#*tupla = ("rojo", "verde", "azul")
#*print(tupla)  #* ("rojo", "verde", "azul")
#*lista = list(tupla)  #* Convierte la tupla en una lista
#*lista[1] = "amarillo"  #* Cambia el segundo elemento
#*tupla_modificada = tuple(lista)  #* Convierte la lista de nuevo en una tupla
#*print(tupla_modificada)  #* ("rojo", "amarillo", "azul")

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver 
# el resultado.
#*my_tuple = (1, 2, 3)
#*del my_tuple
#*print(my_tuple)  #* Esto generará un error porque my_tuple ya no existe.

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar 
# la sintaxis correcta para crear una tupla con un solo elemento.
tupla = (100,)  #* La coma es necesaria para indicar que es una tupla de un solo elemento
print(tupla)  #* (100)
