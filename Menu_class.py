# Usamos una variable Booleana -> Bandera (es True o es False)

control= True

while control == True:
    print("1.Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")

    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            print("1. Papas con salsa")
            print("2. Patacon con hogao")
            print("3. Aros de cebolla")
            print("4. Sopa de tomate")
        case 2:
            print("1. Hamburguesa con papas y gaseosa")
            print("2. Bandeja paisa")
            print("3. Pasta bolognesa")
            print("4. Lasaña")
        case 3:
            print("1. Jugos naturales")
            print("2. Gaseosas marca postobón")
            print("3. Agua")
            print("4. Cerveza")
        case 4:
            print("1. Torta a elección")
            print("2. Helado a elección")
            print("3. Oblea")
            print("4. Postre a elección")
        case 5:
            control = False
        case _:
            print("Opción invalida")

        # El match es para realizar un bucle en forma de menú

        # Bucles infinitos: Para hacer un bucle de la misma manera se elimina el control y en la opción 5.
        # En el case 5 se pone "break" para romper el ciclo.

