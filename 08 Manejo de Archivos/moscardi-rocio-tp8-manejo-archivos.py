#Ejercicio 1
with open("productos.txt", "w") as archivo:
    archivo.write("Zapatillas,12000,5\n")
    archivo.write("Remera,4500,10\n")
    archivo.write("Campera,18000,3\n")

#Ejercicio 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio 3
nombre = input("Ingrese un nuevo producto. ").title().strip()
precio = float(input("Ingrese el precio del producto. "))
cantidad = int(input("Ingrese la cantidad existente del producto. "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

#Ejercicio 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

print()
for producto in productos:
    print(producto)

#Ejercicio 5
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0].strip().lower(),
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

print()
buscado = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()

encontrado = False

for producto in productos:
    if producto["nombre"] == buscado:
        print(f"Producto: {producto['nombre'].title()} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

#Ejercicio 6
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre'].title()},{p['precio']},{p['cantidad']}\n")

print("\nLista final de productos:")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
