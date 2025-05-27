#Práctica de clase: Tienda3

#Este programa maneja el inventario de una tienda con nuevas funcionalidades.

#Isaac Alfonso Rodriguez
#<ialfonsor@academia.usbbog.edu.co>

class Producto:
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def calcula_precio(self, cantidad):
        return self.precio * cantidad

    def inventario_precio(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} | {self.cantidad} unidades | {self.precio} pesos | {self.descripcion[:10]}... | {self.clasificacion} | {self.inventario_precio()} pesos | {self.calcula_precio(5)} pesos"

def ingresar_productos():
    productos = []
    num_productos = int(input("> Cuantos productos va a ingresar?\n< "))
    for i in range(1, num_productos + 1):
        print(f"> Producto {i}, cual es el nombre?")
        nombre = input("< ")
        precio = int(input(f"> cual es el precio de '{nombre}'?\n< "))
        cantidad = int(input(f"> que cantidad hay de '{nombre}'?\n< "))
        descripcion = input(f"> introduzca la descripción de '{nombre}':\n< ")
        clasificacion = input(f"> qué clasificación tiene '{nombre}'?\n< ")
        productos.append(Producto(nombre, precio, cantidad, descripcion, clasificacion))
    return productos

def mostrar_resumen(productos):
    print("\n> Resumen:")
    print("|Producto |Cantidad     |Precio     |Descripción  |Clasificación |Total en inventario |Precio x5 unidades |")
    for producto in productos:
        print(f"|{producto.nombre:<10}|{producto.cantidad:<12} unidades |{producto.precio:<10} pesos |{producto.descripcion[:10]}... |{producto.clasificacion:<12} |{producto.inventario_precio():<18} pesos |{producto.calcula_precio(5):<16} pesos |")

def resumen_precio_por_clasificacion(productos):
    resumen = {}
    for producto in productos:
        if producto.clasificacion not in resumen:
            resumen[producto.clasificacion] = 0
        resumen[producto.clasificacion] += producto.calcula_precio(5)
    
    print("\n> Precios por clasificación")
    print("|Clasificación |Precio     |")
    for clasificacion, total in resumen.items():
        print(f"|{clasificacion:<13} |{total:<10} pesos |")

# Ejecutar el programa
productos = ingresar_productos()
mostrar_resumen(productos)
resumen_precio_por_clasificacion(productos)
