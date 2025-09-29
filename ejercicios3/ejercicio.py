# Compara si el numero 10 es igual a 100
print(10 == 100) 
# Verifica si la cadena 'Hola' es diferente a 'hola'
print('Hola' != 'hola')
# Compara si 15 es mayor que 20
print(15 > 20)
# Verifica si 50 es menor o igual que 100
print(50 <= 100)
# Escribe un codigo que diga si una persona con edad 17 es  mayor de edad(18+)
edad = 17
verificacion = edad >= 18
print(verificacion)
# Compara si la longitud de la palabra 'computadora' es igual a 11
palabra = 'computadora'
longitud = len(palabra) == 11  
# Usamos len() para obtener la longitud del string
print(len(palabra))
print(longitud)
print(type(longitud))
# Verifica si la suma de 7 + 5 es distinta a 12
suma = 7 + 5
numero = 12
print(suma != numero)
# Escribe un codigo que verifique si un usuario ingreso la contraseña 
# correcta ('clave123'), ignorando mayusculas
contraseña = 'clave123'
pregunta_contraseña = input('ingresa la contraseña: ').lower()
verificacion = contraseña == pregunta_contraseña 
print(verificacion)
# Verifica si la nota de un estudiante (75) es suficiente para aprobar (minimo 70)
nota = 75
promedio_aprovatorio = 70
promedio = nota >= 70
print(promedio)
# Compara si dos variables, a = 3.0 y b = 3, son iguales en valor
a = 3.0
b = 3
son_iguales = a == b
print( son_iguales)