# Determinar si un número es par o impar
# Leer número
numero = int(input("Ingresa un número entero:"))
resiudo = numero % 2
#Si residuo es cero es par
if residuo == 0:
    print(numero, " es par")
else:
    print(numero, "es impar")
    