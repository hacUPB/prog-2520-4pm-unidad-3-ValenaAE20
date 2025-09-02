# Desde 5 hasta 20, de uno en uno
for i in range(5,20,1):
    print(i)

# Desde 20 hasta 0, de uno en uno decreciendo:
for i in range(20,-1,-1):
    print(i)

# Desde 0 hasta -20, de uno en uno (también se puede con números negativos):
for i in range(0,-21,-1):
    print(i)

# Ejercicio con error: (No se puede con punto flotante, solo con NÚMEROS ENTEROS).
for i in range(5.0,10.0,0.1):
    print(i)

# Ejercicio 2: Imprimir un número de veces un mensaje.
mensaje = "Programación con Python"
numero = int(input("Ingrese el número: "))

for i in range(numero):
    print(f"{i+1}. {mensaje}")

# Ejercicio 3: Suma de números pares.
numero = int(input("Ingrese un número entero positivo: "))
for i in range(numero+1):
    if i % 2 == 0:
        acumulador += i         # Tipo de variable: acumulador. (También se puede escribir como acumulador = acumulador + i).

print(f"La suma d los pares hasta {numero} es {acumulador}")

# Ejercicio 4: 

'''
1
12
123
1234
12345

i              j
1 hasta n      1 hasta i

'''

numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1):
    for j in range(1, i+1):
        print(j,end=' ')
    print()

    