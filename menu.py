## Tarea

print("Ingrese la zona de envío. Elija un número")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un número: "))
if zona > 0 and zona < 6:
    peso = int(input("Ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
        match zona:
            case 1:
                 total = peso * 11
            case 2:
                 total = peso * 10
            case 3:
                 total = peso * 12
            case 4:
                 total = peso * 24
            case 5:
                 total = peso * 27
            case 6: zona = False
            case _:
             print("Número de zona seleccionado es inválido")
    else:
         print(f"El envío de su paquete cuesta ${total}. ") 
         print("No se puede enviar paquetes de más de 5kg")

