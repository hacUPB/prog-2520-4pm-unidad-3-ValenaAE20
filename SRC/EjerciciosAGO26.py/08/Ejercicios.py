## Ejercicio 1

print(10 > 5)
print("Hola" != "Mundo")
print(3.14 <= 4.5)
nombre = "Juan"
print(nombre == "Juan")

## Ejercicio 2

envio = 0
compra = int(input("Ingrese el valor de la compra>> "))
if compra < 100000:
	envio = 9000
total = compra + envio
print(f"El total de la compra es {total}")

## Ejercicio 3

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 26:
        if edad <= 18:
            etapa = "Adolescencia"
        if edad >= 14:
            etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    print(f"Tu etapa del ciclo de vida es: {etapa}")
else:
    print("La edad ingresada no es válida.")

## Ejercicio 4

print("Ingrese la zona de envío. Elija un número")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un número: "))
if zona > 0 and zona < 6:
    peso = int(input("Ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
        if zona == 1:
            total = peso * 11
    elif zona == 2:
        total = peso * 10
    elif zona == 3:
        total = peso * 12
    elif zona == 4:
        total = peso * 24
    elif zona == 5:
        total = peso * 27
        print(f"El envío de su paquete cuesta ${total}. ") 
        print("No se puede enviar paquetes de más de 5kg")
    else:
        print("La zona ingresada no existe. ")