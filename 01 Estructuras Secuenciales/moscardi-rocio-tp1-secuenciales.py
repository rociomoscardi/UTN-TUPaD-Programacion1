#Ejercicio 1
print("Hola Mundo! \n")

#Ejercicio 2
nombre = input("Ingrese su nombre")

print(f"Hola {nombre}! \n")

#Ejercicio 3
nombre = input("Ingrese su nombre")
apellido = input ("Ingrese su apellido")
edad = int(input("Ingrese su edad"))
lugar_residencia = input("Ingrese su lugar de residencia")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia} \n")

#Ejercicio 4
radio = float(input("Ingrese el radio de un círculo"))

area = 3.14 * radio**2
diametro = 2 * radio
perimetro = diametro * 3.14

print(f"El area del círculo es {area:.2f}cm² y su perímetro es de {perimetro:.2f}cm \n")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos"))

horas = segundos // 60

print(f"{segundos} segundos equivalen a {horas} horas. \n")

#Ejercicio 6
num = int(input("Ingrese un número entero"))

print(num , " * 1 = " , num * 1 , "\n" ,
      num , " * 2 = " , num * 2 , "\n" ,
      num , " * 3 = " , num * 3 , "\n" ,
      num , " * 4 = " , num * 4 , "\n" ,
      num , " * 5 = " , num * 5 , "\n" ,
      num , " * 6 = " , num * 6 , "\n" ,
      num , " * 7 = " , num * 7 , "\n" ,
      num , " * 8 = " , num * 8 , "\n" ,
      num , " * 9 = " , num * 9 , "\n" ,
      num , " * 10 = " , num * 10 , "\n "
      )

#Ejercicio 7
num1 = float(input("Ingrese un número distinto a 0"))
num2 = float(input("Ingrese otro número distinto a 0"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"El resultado de sumar ambos número es {suma:.2f} \n El resultado de restar ambos números es {resta:.2f} \n El resultado de multiplicar ambos números es {multiplicacion:.2f} \n El resultado de dividir ambos números es {division:.2f} \n")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros"))
peso = float(input("Ingrese su peso en kilos"))

imc = peso / altura**2

print(f"Su IMC es {imc:.2f} \n")

#Ejercicio 9
celsius = float(input("Ingrese una temperatura en grados Celsius"))

farenheit = celsius * 9/5 + 32

print(f"{celsius} grados Celsius equivalen a {farenheit} grados Farenheit. \n")

#Ejercicio 10
num3 = float(input("Ingrese un número"))
num4 = float(input("Ingrese el siguiente número"))
num5 = float(input("Ingrese el último número"))

promedio = (num3 + num4 + num5) / 3

print(f"El promedio de los números ingresados es {promedio:.2f} \n")