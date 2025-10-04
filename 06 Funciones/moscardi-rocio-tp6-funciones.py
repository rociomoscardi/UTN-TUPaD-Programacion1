#Ejercicio 1
def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

nombre = input("Ingrese su nombre. ")

print(saludar_usuario(nombre))

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = input("Ingrese su nombre. ").title()
apellido = input("Ingrese su apellido. ").title()
edad = int(input("Ingrese su edad. "))
residencia = input("Ingrese su país de residencia. ").title()

print(informacion_personal(nombre, apellido, edad, residencia))

#Ejercicio 4
import math

def calcular_area_circulo(radio):
    return (radio**2) * math.pi

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo en centímetros. "))

print(f"Área del círculo: {calcular_area_circulo(radio):.2f} cm²")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f} cm²")

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese una cantidad de segundos. "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")

#Ejercicio 6
def tabla_multiplicar(numero):
    return f"{numero} x 1 = {numero * 1}\n{numero} x 2 = {numero * 2}\n{numero} x 3 = {numero * 3}\n{numero} x 4 = {numero * 4}\n{numero} x 5 = {numero * 5}\n{numero} x 6 = {numero * 6}\n{numero} x 7 = {numero * 7}\n{numero} x 8 = {numero * 8}\n{numero} x 9 = {numero * 9}\n{numero} x 10 = {numero * 10} "

numero = int(input("Ingrese un número. "))

print(tabla_multiplicar(numero))

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division) 

a = float(input("Ingrese el primer número. "))
b = float(input("Ingrese el segundo número. "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]:.2f}")

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingrese su peso en kilogramos. "))
altura = float(input("Ingrese su altura en metros. "))

print(f"Su índice de masa corporal (IMC) es {calcular_imc(peso, altura):.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Ingrese una temperatura en grados Celsius. "))

print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit.")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número. "))
b = float(input("Ingrese el segundo número. "))
c = float(input("Ingrese el tercer número. "))

print(f"El promedio de los tres números ingresados es: {calcular_promedio(a, b, c):.2}")
