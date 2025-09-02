#Ejercicio 1
for i in range(101):
    print(i)

#Ejercicio 2
num = abs(int(input("Ingrese un número entero.")))
digitos = 0

while num > 0:
    digitos += 1
    num = num // 10  

print(f"El número que usted ingresó contiene {digitos} dígito/s")

#Ejercicio 3
num1 = int(input("Ingrese un número entero."))
num2 = int(input("Ingrese otro número entero."))
suma = 0

for i in range (num1+1, num2):
    suma = i + suma

print (f"La suma de los números comprendidos entre {num1} y {num2} da como resultado {suma}.")

#Ejercicio 4
total = 0
num = float('inf')

while num != 0:
    num = int(input("Ingrese un número entero."))
    total = total + num

print(f"El total acumulado es de {total}.")

#Ejercicio 5
import random

aleatorio = random.randint(0, 9)
intentos = 1
num = int(input("Intente adivinar el número del 0 al 9."))

while num != aleatorio:
    num = int(input("Intente adivinar el número del 0 al 9."))
    intentos = intentos + 1 

print(f"El número era {aleatorio}! Te tomó {intentos} intento/s adivinarlo.")

#Ejercicio 6
for i in range(100, 0, -2):
    print(i)

#Ejercicio 7
num = int(input("Ingrese un número entero."))
suma = 0

for i in range (num):
    suma = i + suma

print (f"La suma de los números comprendidos entre 0 y {num} da como resultado {suma}.")

#Ejercicio 8
total = 5 #Para que procese 100 números basta con cambiar el 5 por el número 100.
num = 0
par = 0
impar = 0 
negativo = 0 
positivo = 0

for i in range (total):
    num = int(input("Ingrese un número entero."))

    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    if num > 0:
        positivo = positivo + 1
    else: 
        negativo = negativo + 1 


print(f"Cantidad de números pares: {par}. \nCantidad de números impares: {impar}. \nCantidad de números negativos: {negativo}. \nCantidad de números positivos: {positivo}.")

#Ejercicio 9
total = 5 #Para que procese 100 números basta con cambiar el 5 por el número 100.
num = 0
suma = 0

for i in range (total):
    num = int(input("Ingrese un número entero."))
    suma = num + suma

print(f"La media de los valores ingresados es: {suma / total}")

#Ejercicio 10
num = int(input("Ingrese un número."))
digito = 0 
invertido = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(f"El número invertido es: {invertido}.")