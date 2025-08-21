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
   print("Peso bajo")
else:
   if IMC <= 24.99:
      print("Peso normal")
    else:
      if IMC <= 