lista = [item for item in range(11)]

def es_multiplo(x):
    return x % 3 == 0
lista2 = list(filter(es_multiplo, lista))
print(lista2)


# Alternativa usando lambda
lista3 = list(filter(lambda x: x % 3 == 0, lista))
print(lista3)

lista = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

set = {item for item in lista if item % 2 == 0}
print(set)

posiciones = {'LH': 1, 'MV': 2, 'SP': 3, 'VB': 4, 'FA': 5, 'CL': 6}

print(posiciones.items())

print('Diccionario de posiciones:')
for key, value in posiciones.items():
    print(f'La posición {key} es {value}')

print('\nDiccionario organizado alfabéticamente por keys:')
for key, value in sorted(posiciones.items(),reverse=True):
    print(f'{key}:{value}')

posiciones1 = {'LH': 1, 'MV': 2, 'SP': 3, 'VB': 4, 'FA': 5, 'CL': 6}
posiciones2 = {'MV': 2, 'LH': 1, 'VB': 4, 'SP': 3, 'CL': 6, 'FA': 5}
posiciones3 = {'VB': 1, 'SP': 2, 'MV': 3, 'CL': 4, 'LH': 5, 'FA': 6}
def comparar_diccionarios(dict1, dict2):
    return dict1 == dict2
print('\nComparando posiciones1 y posiciones2:')
print(comparar_diccionarios(posiciones1, posiciones2))
