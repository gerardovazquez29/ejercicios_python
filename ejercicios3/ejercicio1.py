
# Verifica si un número es positivo y par.
num = 5
if num % 2 == 0 and num >= 0:
    print(f'El numero: {num} es positivo y es par')
elif num % 2 == 0 or num >= 0:
    print(f'El numero: {num} no es par y es positivo')
else:
    print(f'El numero: {num} no es positivo ni es par')

# Comprobar si un usuario ingresó correctamente el usuario o la contraseña.
usuario = 'gerardo1'
contraseña = 1234
usuario_almacenado = 'gerardo'
contraseña_almacenada = 1234  

if contraseña == contraseña_almacenada and usuario == usuario_almacenado:
    print('acseso consedido')
else:
    print('acceso denegado')

# Verifica si una persona puede votar (edad >= 18) y tiene INE.
persona = 18
tiene_ine = False
if persona >= 18 and tiene_ine:
    print('Puede votar')
else:
    print('No puede votar')

# Determina si una persona puede entrar a una fiesta: 
# si es mayor de edad o está acompañado por un adulto.
persona = 16
acompañado_adulto = True
if persona >= 18:
    print('Puede entrar ala fiesta sin restricciones')
elif persona < 18 and acompañado_adulto:
    print('Puede entrar con adulto pero no puede consumir alcohol')
else:
    print('No puede entrar ala fiesta ')

# Verifica si un número NO está entre 100 y 200.
numero = 50
if numero >= 100 and numero <= 200:
    print('El numero esta entre el 100 y el 200')
else:
    print('El numero no esta entre el 100 y el 200')

# Validar si un usuario no está bloqueado y su cuenta está activa.

usuario_bloqueado = False
cuenta_activa = False
if not usuario_bloqueado and cuenta_activa:
    print('Tiene acceso')
elif not usuario_bloqueado or cuenta_activa:
    print('No tiene acceso  su cuenta esta bloqueada')
else:
    print('No tiene acceso el usuario esta bloqueado')

# Verifica si un número es divisible 
# por 3 o por 5 pero no ambos (usa lógica exclusiva)
numero = 10
  
if (numero % 3 == 0) and (numero % 5 != 0):
    print('El numero es divisible entre 3 pero no de 5')
elif (numero % 5 == 0) and (numero % 3 != 0):
    print('El numero es divisible entre 5 pero no de 3')
else:
    print('el numero es divisible por ambos o por ninguno')

# Validar si una cadena de texto no está vacía 
# y tiene más de 5 caracteres
texto = 'cade'
longitud = len(texto)
if longitud > 0 and longitud > 5:
    print('la cadena de texto no esta vacia y tiene mas de 5 caracteres')
else:
    print('No cumple con lo requerido')

