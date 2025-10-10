# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario luego de añadir frutas:")
print(precios_frutas)
print()

# Ejercicio 2
# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario luego de actualizar precios:")
print(precios_frutas)
print()

#Ejercicio 3
print("Listado de frutas: ")
print(precios_frutas.keys())

#Ejercicio 4
numeros_telefonicos = {}
nombre = ""
numero = ""

for i in range (5):
    nombre = input("Ingrese el nombre del contacto que desea agregar. ").title().strip()
    numero = input("Ingrese el número del contacto que desea agregar. ").strip()

    numeros_telefonicos[nombre] = numero

print(numeros_telefonicos)

nombre = input("Ingrese el nombre del contacto para consultar su número. ").title().strip()

if nombre in numeros_telefonicos:
    print(numeros_telefonicos[nombre])
else:
    print("El nombre ingresado no está en su lista de contactos.")

#Ejercicio 5
frase = input("Ingrese una frase. ")

palabras = frase.split()

palabras_unicas = set(palabras)

repeticiones = {}
for palabra in palabras_unicas:
    repeticiones[palabra] = palabras.count(palabra)

print(f"Usted ingresó la frase: '{frase}'")

print(f"La frase cuenta con las palabras: {palabras}")

print(f"Cantidad de veces que aparece cada palabra: {repeticiones}")

#Ejercicio 6 
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

#Ejercicio 7
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105, 106}

print(f"Alumnos que aprobaron ambos parciales: {parcial1 & parcial2}")
print(f"Alumnos que aprobaron o el parcial 1 o el parcial 2: {parcial1 ^ parcial2}")
print(f"Alumnos que aprobaron al menos un parcial: {parcial1 | parcial2}")

#Ejercicio 8
stock = {'Televisión': 20, 'Escritorio': 50, 'Silla': 30}

print(stock)
print()

while True:
    opcion = input("Seleccione una de las siguientes opciones: " \
    "\n1. Consultar el stock de un producto. " 
    "\n2. Agregar unidades a un producto. " 
    "\n3. Agregar un nuevo producto. " 
    "\n4. Consultar disponibilidad. "  
    "\n5. Salir. ")
    seleccion = int(opcion)

    match seleccion:
        case 1:
            producto = input("Ingrese un producto para consultar su stock. ").title().strip()

            if producto in stock:
                print(stock[producto])
            else:
                print("El producto ingresado no está en su lista de stock.")
                continue
        case 2:
            producto = input("Ingrese un producto para agregar unidades a su stock. ").title().strip()
            unidades = int(input("Ingrese la cantidad de unidades que desea agregar. "))

            stock[producto] = stock[producto] + unidades

            print("Lista actualizada: ")
            print(stock)
            print()
            continue
        case 3:
            producto = input("Ingrese un producto para agregarlo a su lista. ").title().strip()
            unidades = int(input("Ingrese la cantidad de unidades que tiene en stock del producto. "))

            stock[producto] = unidades

            print("Lista actualizada: ")
            print(stock)
            print()
        case 4:
            producto = input("Ingrese un producto para consultar su disponibilidad. ").title().strip()
            
            if producto in stock:
                print(f"'{producto}' disponible. En stock: {stock[producto]}. ")
            else:
                print(f"'{producto}' no se encuentra disponible. ")
            continue
        case 5:
            print("Saliendo...")
            break

#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "06:00"): "Gimnasio",
    ("sábado", "21:00"): "Cumpleaños"
}

dia = input("Ingresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}.")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Colombia": "Bogotá"}
print(original)

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)
