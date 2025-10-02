# Ejercicicos

""" 1-Escribe es_primo(n) que devuelva True si n es primo; 
usa un return temprano cuando encuentres un divisor. """
def es_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        """
        info: n ** 0.5 = Raíz cuadrada de n

                Ejemplo: Si n = 15, entonces 15 ** 0.5 = 3.87...
                int(n ** 0.5) = Parte entera de la raíz cuadrada
                Ejemplo: int(3.87) = 3
                int(n ** 0.5) + 1 = Le suma 1 para incluir ese número en el rango
                Ejemplo: 3 + 1 = 4
                range(2, 4) = Genera los números [2, 3] (el 4 no se incluye)
        """
        if n % i == 0:
            return False
    return True
print(es_primo(15)) # False
print(es_primo(17)) # True

# 2-Implementa maximo(*valores) sin usar max() incorporado.


""" 3-Crea un conversor genérico 
convertir_temperatura(valor, origen="C", destino="F") 
que acepte combinaciones C/F/K. """


""" 4-Programa un decorador temporizar que imprima 
cuánto tarda en ejecutarse la función decorada. """


""" 5-Diseña contador_palabras(texto, **opciones) 
donde opciones acepte minusculas=True/False y solo_unicas=True/False. """


# 6-Genera con lambda y filter los números divisibles por 3 y 5 del 1 al 100.


""" 7-Construye una closure generador_de_potencias(exp) 
que devuelva una función que eleve a exp. """


""" 8-Añade anotaciones de tipo a la función de IMC y usa mypy 
(si lo tienes) para verificar. """


""" 9-Practica documentar con docstrings estilo Google o NumPy 
en al menos dos funciones previas. """


""" 10-Reescribe area_rectangulo para aceptar tanto tuplas 
(base, altura) como dos números, usando sobrecarga 
con inspección de tipos. """
