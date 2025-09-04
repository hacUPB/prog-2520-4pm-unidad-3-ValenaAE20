# Ejemplo: Con Random usando bucle While.
# Import random
from random import randint

#num_aleatorio = random.randint(0,50)
num_aleatorio = randint(0,50)    #randint genera un número aleatorio en ese rango (en este caso 0,50).

# Ejercicio: Adivina el número

'''
Variable de entrada
Nombre        Tipo
numero        int

Variable de salida
Intentos      int     contador

Variable de control
numero        int
'''

# num_aleatorio = random.randint(0,50)
num_aleatorio = randint(1,100)
intentos = 0
numero = -1    #Un número diferente a los números aleatorios, obliga a entrar al while la primera vez.

while numero != num_aleatorio:
    numero = int(input("Adivina el número oculto entre 1 y 100: "))
    intentos += 1
    if numero > num_aleatorio:
        print("El número oculto es menor")
    elif numero < num_aleatorio:
        print("El número oculto es mayor")
    else:
        print("Felicidades, adivinaste...")
print(f"Adivinaste en {intentos} intentos")

