"""
Ejercicio6
    - Mostrar todas las tablas de multiplicar del 1 al 10.
    - Mostrando el titulo de la tabla y luego las multiplicaciones
      del 1 al 10
"""
for cabecera in range(1,11):
    print("#"*21)
    print(f"#### Tabla del {cabecera} ####")
    print("#"*21)
    for numero in range(1,11):
        print(f"{numero} X {cabecera} = {numero * cabecera}")
    print("\n")

