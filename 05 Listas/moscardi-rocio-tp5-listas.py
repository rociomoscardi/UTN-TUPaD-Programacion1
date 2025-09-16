#Ejercicio 1
notas = [6, 9, 7, 5, 10, 9.5, 4, 8, 6, 7.5]
suma = 0

for nota in notas:
    print(nota)

    suma = nota + suma

promedio = suma / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
    
#Ejercicio 2
productos = []

for i in range (5):
    productos.append(str(input("Ingrese un producto.")))

print(sorted(productos))

opcion = int(input("Elija una de las siguientes opciones: \n 1. Si desea eliminar un producto. \n 2. Si quiere salir del programa."))

if opcion == 1:
    productos.remove(str(input("Escriba el producto que desea eliminar.")))
    print(sorted(productos))
elif opcion == 2:
    exit
else:
    print("Por favor, seleccione una opción válida.")
    
#Ejercicio 3
import random

numeros = [random.randint(1, 100) for i in range(15)]
print("Lista completa:", numeros)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista de pares:", pares)
print("Lista de impares:", impares)
print("La lista de pares contiene", len(pares), "números.")
print("La lista de impares contiene", len(impares), "números.")

#Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

print("Datos:", datos)

for dato in datos:
    if dato not in sin_repetidos:
        sin_repetidos.append(dato)

print("Nueva lista sin elementos repetidos:", sin_repetidos)

#Ejercicio 5
presentes = ["Nahuel", "Rocío", "Silvana", "Jorge", "Esteban", "Lola", "Federico", "Camila"]
print(presentes)

opcion = int(input("Elija una de las siguientes opciones: \n 1. Si quiere agregar un nuevo estudiante. \n 2. Si quiere eliminar un estudiante. \n 3. Si no quiere realizar ninguna de las acciones anteriores."))

if opcion == 1:
    presentes.append(str(input("Ingrese el nombre del estudiante a agregar.")))
    print(presentes)
elif opcion == 2:
    presentes.remove(str(input("Ingrese el nombre del estudiante a eliminar.")))
    print(presentes)
elif opcion == 3:
    exit
else:
    print("Por favor, seleccione una opción válida.")

#Ejercicio 6
numeros = [10, 20, 30, 40, 50, 60, 70]
rotada = [numeros[-1]] + numeros[:-1]

print(numeros)
print(rotada)

#Ejercicio 7
temperaturas = [
    ["Lunes", 9, 20],
    ["Martes", 12, 26],
    ["Miércoles", 10, 22],
    ["Jueves", 8, 19],
    ["Viernes", 11, 25],
    ["Sábado", 13, 27],
    ["Domingo", 7, 18]
]
print(temperaturas)

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

for dia in temperaturas:
    suma_min = suma_min + dia[1]
    suma_max = suma_max + dia[2]
    
    amplitud = dia[2] - dia[1]
    if amplitud > mayor_amplitud:
            mayor_amplitud = amplitud
            dia_mayor_amplitud = dia[0]

prom_minimas = suma_min / len(temperaturas)
prom_maximas = suma_max / len(temperaturas)

print("El promedio de las temperaturas mínimas es:", prom_minimas)
print(f"El promedio de las temperaturas máximas es: {prom_maximas:.2f}")
print("Se registró mayor amplitud térmica el día", dia_mayor_amplitud)

#Ejercicio 8
notas_estudiantes = [
    ["Laura", 8, 7, 9],
    ["Sofía", 5, 9, 7],
    ["Emanuel", 10, 8, 7],
    ["Juan", 7, 8, 10],
    ["Milagros", 8, 6, 7]
]

print(notas_estudiantes)
suma_notas = 0

for alumno in notas_estudiantes:
    nombre = alumno[0]
    notas = alumno[1:]
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

materias = 3
for i in range(1, materias + 1): 
    for alumno in notas_estudiantes:
        suma_notas = suma_notas + alumno[i]
    promedio = suma_notas / len(notas_estudiantes)
    print(f"Promedio de la materia {i}: {promedio:.2f}")

#Ejercicio 9
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

while True:
    fila = int(input("Ingresá la fila (0-2): "))
    columna = int(input("Ingresá la columna (0-2): "))
    simbolo = input("Ingresá tu símbolo (X u O): ")

    # Verifico si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = simbolo
    else:
        print("Esa casilla ya está ocupada. Elegí otra.")
        continue 


    for f in tablero:
        print(" ".join(f))

    
    salir = input("¿Querés seguir jugando? (s/n): ")
    if salir.lower() == "n":
        break

#Ejercicio 10
ventas = [
    [5, 3, 6, 2, 4, 7, 1],  # Televisión
    [2, 4, 3, 5, 6, 2, 3],  # Cama
    [1, 2, 4, 3, 5, 6, 2],  # Sillón
    [3, 5, 2, 4, 1, 3, 4]   # Escritorio
]
productos = ["Televisión", "Cama", "Sillón", "Escritorio"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    print(f"{productos[i]}: Total vendido = {total_producto}")

mayor_total = 0
dia_mayor = ""

for j in range(7):  # 7 días
    total_dia = 0
    for i in range(4):  # 4 productos
        total_dia += ventas[i][j]
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = dias[j]

print(f"Día con mayores ventas: {dia_mayor} con {mayor_total} unidades")

mayor_ventas = 0
producto_top = ""

for i in range(4):
    total = sum(ventas[i])
    if total > mayor_ventas:
        mayor_ventas = total
        producto_top = productos[i]

print(f"Producto más vendido: {producto_top} con {mayor_ventas} unidades")
