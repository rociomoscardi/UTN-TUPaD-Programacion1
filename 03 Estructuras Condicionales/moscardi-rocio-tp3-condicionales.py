#Ejercicio 1
edad1 = int(input("Ingrese su edad."))

if edad1 > 18:
    print("Es mayor de edad.")

#Ejercicio 2
nota = float(input("Ingrese su nota."))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Ejercicio 3
num = int(input("Ingrese un número par."))

if num%2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Ejercicio 4
edad4 = int(input("Ingrese su edad."))

if edad4 < 12:
    print("Niño/a.")
elif edad4 >= 12 and edad4 <= 18:
    print("Adolescente.")
elif edad4 >= 18 and edad4 < 30:
    print ("Adulto/a joven.")
elif edad4 >= 30:
    print ("Adulto/a")

#Ejercicio 5
contrasenia = str(input("Ingrese su contraseña."))
length = len(contrasenia)

if length >= 8 and length <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo.")
elif media == mediana == moda:
    print("No hay sesgo.") 
else:
    print("Distribución no claramente sesgada.")

#Ejercicio 7
frase_palabra = str(input("Ingrese una frase o palabra.")).lower()
ultima_letra = frase_palabra[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase_palabra}!")
else:
    print(frase_palabra)

#Ejercicio 8
nombre = str(input("Ingrese su nombre."))
opcion = int(input("Elija una de las siguientes opciones: \n 1. Si quiere su nombre en mayúsculas. \n 2. Si quiere su nombre en minúsculas. \n 3. Si quiere su nombre con la primera letra mayúscula."))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Por favor, seleccione una opción válida.")

#Ejercicio 9 
magnitud = int(input("Ingrese la magnitud del terremoto para clasificarlo según la escala de Ritcher."))

if magnitud < 3:
    print("Muy leve, imperceptible.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, ligeramente perceptible.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado, sentido por personas pero generalmente no causa daños.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte, puede causar daños en estructuras débiles.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte, puede causar daños significativos.")
elif magnitud >= 7:
    print("Extremo, puede causar graves daños a gran escala.")

#Ejercicio 10
#Declaramos las variables y le pedimos al usuario que ingrese los datos a almacenar.
hemisferio = str(input("Ingrese el hemisferio en el que se encuentra (Norte / Sur).")).title()
mes = int(input("Ingrese el número del mes actual (1-12)."))
dia = int(input("Ingrese el número del día actual (1-31)."))
datos_validos = True

#Validamos que todos los datos sean correctos.
if hemisferio not in ["Norte", "Sur"]:
    print("El hemisferio ingresado no es válido. Debe ser 'Norte' o 'Sur'.")
    datos_validos = False

if not (mes >= 1 and mes <= 12):
    print("El número de mes ingresado no es válido. Debe estar entre 1 y 12.")
    datos_validos = False

if not (dia >= 1 and dia <= 31):
    print("El número de día ingresado no es válido. Debe estar entre 1 y 31.")
    datos_validos = False

#Si los datos son correctos, procedemos a compararlos para determinar la estación del año.
if datos_validos:
    if (hemisferio == "Norte" or hemisferio == "Sur") and (mes >= 1 and mes <= 12) and (dia >= 1 and dia <= 31):
        if hemisferio == "Norte":
            if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
                print("Usted está en invierno.")
            elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
                print("Usted está en primavera.")
            elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
                print("Usted está en verano.")
            elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
                print("Usted está en otoño.")
        elif hemisferio == "Sur":
            if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
                print("Usted está en verano.")
            elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
                print("Usted está en otoño.")
            elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
                print("Usted está en invierno.")
            elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
                print("Usted está en primavera.")
