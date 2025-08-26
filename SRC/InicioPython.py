print ("Por favor ingrese su nombre: ")
nombre = input()
print ("Bienvenido ", nombre)

#Calculcar el índice de Masa Corporal
#IMC = peso / estatura^2

#Leer estatura
estatura = input("Ingrese su estatura en metros: ")
estatura = float(estatura)
#Leer peso
peso = input("Ingrese su peso en kilogramos: ")
peso = float(peso)
#Calcular IMC
IMC = peso / estatura ** 2
#Mostrar IMC
print("Su IMC = ", IMC)
        
#Tabla de IMC
if IMC < 18.49:
    mensaje = "Bajo peso"
elif IMC < 25:
    mensaje = "Normal"
elif IMC < 30:
    mensaje = "Sobrepeso"
elif IMC < 35:
    mensaje = "Obesidad tipo 1"
elif IMC < 40:
    mensaje = "Obesidad tipo 2"
else:
    mensaje = "Obesidad extrema"
print(f"{nombre}, su IMC es {IMC} y su condición es {mensaje}.")