# Ejercicio 1
'''precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

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
print(precios_frutas.keys())'''

#Ejercicio 4
numeros_telefonicos = {}
nombre = ""
numero = ""

for i in range (2):
    nombre = input("Ingrese el nombre del contacto que desea agregar. ")
    numero = input("Ingrese el número del contacto que desea agregar. ")

    numeros_telefonicos[nombre] = numero

print(numeros_telefonicos)

nombre = input("Ingrese el nombre del contacto para consultar su número. ")

if nombre in numeros_telefonicos:
    print(numeros_telefonicos[nombre])
else:
    print("El nombre ingresado no está en su lista de contactos.")

#Ejercicio 5


