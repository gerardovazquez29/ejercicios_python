a = 6
b = 6
resultado = a == b
print(resultado)

temperatura = 25
if temperatura > 30:
    print('Hace mucho calor')
else:
    print('No hace tanto calor')

edad = 17
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print('Puedes conducir legalmente')
    else:
        print('Eres mayor pero no tienes licencia')
else:
    print('No puedes conducir legalmente')

hora = 14
es_fin_semana = True

if hora >= 8 and hora <= 18 and not es_fin_semana:
    print('Horario laboral')
else:
    print('Fuera de Horario laboral')


numero = int(input('Ingresa un numero '))
if numero >0:
    print('Es positivo')
else:
    print('Es negativo')


# Pide un número al usuario y determina si es par o impar

es_par = int(input('ingresa un numero '))
if es_par % 2 == 0:
    print(f'el numero {es_par} es par')
else:
    print(f'el numero {es_par} es impar')


# Determina si un año ingresado por el usuario es bisiesto o no

anio = int(input('Ingresa un año: '))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f'El año: {anio} Si es bisiesto.')
else:
    print(f'El año: {anio} No es bisiesto.')
