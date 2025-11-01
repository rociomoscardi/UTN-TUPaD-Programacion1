#Ejercicio 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular los factoriales del 1 al número ingresado: "))

if num == 0:
    print("Factorial de 0 = 1")
else:
    for i in range(1, num+1):
        print(f"Factorial de {i} = {factorial(i)}")

# Ejercicio 2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)

num = int(input("Ingrese un número para mostrar la serie de Fibonacci hasta esa posición: "))

if num == 0:
    print("Fibonacci = 0")
elif num == 1:
    print("Fibonacci = 1")
else:
    for i in range(1, num+1):
        print(f"Fibonacci en posición {i} = {fibonacci(i)}")

# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
num_base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente == 0:
    print(f"{num_base} elevado a la 0 = 1")
elif exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = potencia(num_base, exponente)
    print(f"{num_base} elevado a la {exponente} = {resultado}")

# Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
numero = int(input("Ingrese un número entero positivo en base decimal para convertir a binario: "))

if numero < 0:
    print("El número debe ser positivo.")
else: 
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
texto = input("Ingrese una palabra sin espacios ni tildes para verificar si es palíndromo: ").lower().strip()

if texto == "":
    print("No se ingresó ninguna palabra.")
else:
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else: 
        return (n % 10) + suma_digitos(n // 10)
    
numero = int(input("Ingrese un número positivo para sumar sus digitos: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else: 
        return n + contar_bloques(n - 1)
    
nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

if nivel_base < 1:
    print("Debe ingresar un número entero positivo mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Para construir la pirámide se necesitan {total} bloques.")

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0 a 9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. El número debe ser positivo y el dígito debe estar entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")