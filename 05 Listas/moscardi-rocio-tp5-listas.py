#Ejercicio 1
'''notas = [6, 9, 7, 5, 10, 9.5, 4, 8, 6, 7.5]
suma = 0

for nota in notas:
  print(nota)
  
  suma = nota + suma

promedio = suma / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))'''
    
#Ejercicio 2
'''productos = []

for i in range (5):
  productos.append(str(input("Ingrese un producto.")))

print(sorted(productos))

productos.remove(str(input("Si desea eliminar un producto, escribalo a continuación.")))
print(sorted(productos))'''

#Ejercicio 3
'''import random

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
print("La lista de impares contiene", len(impares), "números.")'''

#Ejercicio 4
'''datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

print("Datos:", datos)

for dato in datos:
    if dato not in sin_repetidos:
        sin_repetidos.append(dato)

print("Nueva lista sin elementos repetidos:", sin_repetidos)'''

#Ejercicio 5
'''presentes = ["Nahuel", "Rocío", "Silvana", "Jorge", "Esteban", "Lola", "Federico", "Camila"]
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
    print("Por favor, seleccione una opción válida.")'''

#Ejercicio 6
'''numeros = [10, 20, 30, 40, 50, 60, 70]
rotada = [numeros[-1]] + numeros[:-1]

print(numeros)
print(rotada)'''

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
