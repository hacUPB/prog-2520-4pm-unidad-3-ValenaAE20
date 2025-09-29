# Ejemplo 1:

numero = 1
while numero <= 5:
    print(numero)
    numero += 1       #numero = numero + 1

# La forma numero +=1 es la forma abreviada de hacer el incremento.
# Y se puede hacer el incremento al número que se necesite sin necesidad de escribir el incremento completo.

# Ejercicio 1: modificar este código para que salgan los números pares entre 20 y 80.

#Solución:

numero = 20
while numero <= 80:
    print(numero)
    numero +=2

# Ejercicio 2: Imprimir los números impares entre 99 y 61. En orden ascendente.
# Explicación: Solicitar 2 números al usuario e imprimir los números impares entre ellos.
# Solución:

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    mayor=num1
    menor=num2
else:
    mayor=num2
    menor=num1
while menor <= mayor:
    if menor % 2==1:
        print(menor)
    menor += 1

# Ejercicio 3: Escribir todos los múltiplos de 7 entre 0 y 100.

#Solución:

numero = 0
while numero <= 100:
    if numero % 7==0:
        print(numero)
    numero += 1

# Ejercicio: Solicitar un número al usuario e imprimir su tabla de multiplicar hasta el 15.

# Solución:

numero = int(input("Ingrese un número entero: "))
tabla = 1
while tabla <= 15:
    resultado = tabla * numero
    print(f"{numero} x {tabla} = {resultado}")
    tabla += 1

    
