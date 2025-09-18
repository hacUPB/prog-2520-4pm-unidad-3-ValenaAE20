# Crear una función que imprima la tabla de cualquier número - bucle for
def tabla(num):
    for i in range(1,11):
        producto = i * num
        print(f"{num} x {i} = {producto}")
    # Esta función anterior no tiene ningún retorno

# Llamando a la función
numero = int(input("Ingrese un valor: "))
var = tabla(numero)

