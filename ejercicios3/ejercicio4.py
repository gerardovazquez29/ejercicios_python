
# Usa bucles para imprimir esta forma:

for i in range(1,6):
    for y in range(1, i + 1):
        print(y, end=" ")
    print()

print("-"* 20)
# Escribe un programa que imprima todos los números 
# primos del 1 al 50 usando bucles.
for num in range(2, 51):
    es_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo= False
            break
    if es_primo:
        print(num, end=" ")
print()
print("-"* 20)
