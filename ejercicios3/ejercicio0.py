edad =10

if edad >= 10 and edad <= 30:
    print('Edad dentro del rango permitido')
else:
    print('tu edad no es permitida')

usuario = True
admin = True

if usuario and admin:
    print('Tiene acceso total')
else:
    print('Acceso limitado')

# Verifica si un número NO está dentro del rango permitido
numero = 150
if not (numero >= 1 and numero <= 100):
    print("Número fuera de rango")

# Validar entrada de un cliente a un sistema
tiene_credencial = True
es_empleado = False
autorizado = True

if (tiene_credencial and autorizado) or es_empleado:
    print("Puede entrar al sistema")
else:
    print("Acceso denegado")
    
# Combinación lógica compleja
edad = 17
permiso_padres = True
acompanado_por_adulto = False

if edad >= 18 or (permiso_padres and acompanado_por_adulto):
    print("Entrada permitida")
else:
    print("Entrada denegada")

hay_movimiento = True
alarma_encendida = False

if hay_movimiento and alarma_encendida:
    print("¡Alarma activada!")
else:
    print("Todo tranquilo.")
    
