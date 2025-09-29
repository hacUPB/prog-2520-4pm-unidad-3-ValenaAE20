# Tarea en casa, unidad 4
# Actividad 1: fundamentos


# Lectura 1: Objetos, Variables y Etiquetas
# Un objeto es como una "cajita" con datos y funciones propias.

# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500

#Conclusión: 
# En Python todo es un objeto. Las variables no guardan el valor como en otros lenguajes, sino que son como etiquetas que apuntan a ese objeto.
# En este caso, si tengo altitud = 10000 y luego digo elevacion = altitud, las 2 etiquetas apuntan al mismo número.
# Pero si después cambio elevacion = 9500, ya no estoy cambiando el valor original, sino que ahora esa etiqueta apunta a otro número, mientras que altitud sigue con el 10000.


# Lectura 2: ID de objetos

velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))

# Conclusión:
# En python, cada objeto tiene un identificador único (como por ejemplo una "cédula"). Ese ID lo podemos ver con la función id().
# Si hago 2 variables con el mismo número, a veces Python las hace apuntar al mismo objeto para ahorrar memoria (sobre todo con números pequeños).
# Pero si creo objetos más grandes, como listas, aunque tengan los mismos valores, cada uno tendrá su propio ID porque son objetos distintos.


# Lectura 3: Mutabilidad vs Inmutabilidad

# Mutabilidad:
#Objetos inmutables: no se pueden cambiar, si los "modifico" en realidad se crea un objeto nuevo.
#Ejemplos: números, strings, tuplas.

#Objetos mutables: Sí se pueden cambiar en el mismo lugar.
#Ejemplos: listas, diccionarios, sets.


# Ejemplo con objetos inmutables (strings):

modelo = "Boeing 747"
print(id(modelo))  # Guardamos el ID original

# Intentamos "modificar" el string
modelo = modelo + "-800" 
print(modelo)  # "Boeing 747-800"
print(id(modelo))  # ¡ID diferente! Se creó un nuevo objeto

# Conclusión:
modelo = "Boeing 747"
modelo = modelo + "-800" # Se crea un nuevo string
# El ID cambia porque es un objeto distinto.


# Ejemplo con objetos mutables (listas):

componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place

# Conclusión:
omponentes = ["alas", "fuselaje", "motores"]
componentes.append("tren de aterrizaje") # Se modifica la lista original
# El ID sigue igual porque el objeto se cambió "en el mismo sitio".


# ¿Cómo afecta la mutabilidad a los objetos que se usan como argumentos de una función?
# Cuando paso un objeto mutable (como una lista) a una función, los cambios sí afectan al original.
# Con un inmutable, no pasa eso.

def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada

# Conclusión:
combustible_actual = [1000, 1200, 800]
agregar_combustible(combustible_actual, 500)
print(combustible_actual) # La lista original cambia
# La mutabilidad define si un objeto se altera o no dentro de una función.


# Iterables e Iteración:
# Un iterable es un objeto que se puede recorrer elemento por elemento (listas, tuplas, sets, diccionarios, archivos, generadores).


#Iteración con bucles for:
# Es la forma más común.

# Iterando sobre una lista de sensores de aeronave
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")


# Iteración con bucles while:
# Menos común, pero útil con contadores.

# Simulando lecturas de altitud cada 10 segundos
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1


# Funciones útiles de iteración:

# enumerate(): da el índice y el valor.

for i, etapa in enumerate(["despegue", "ascenso", "crucero", "descenso", "aterrizaje"]):
    print(f"Etapa {i+1}: {etapa}")

# zip(): recorre varios iterables a la vez.

tiempos = [0, 10, 20, 30]
velocidades = [0, 200, 300, 320]

for t, v in zip(tiempos, velocidades):
    print(f"Tiempo: {t}s - Velocidad: {v} km/h")

# Comprensiones de listas: forma rápida de crear listas. (No las usaremos en evaluaciones o retos de este curso).


