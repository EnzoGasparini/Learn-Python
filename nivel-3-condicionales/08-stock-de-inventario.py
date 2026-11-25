#Stock de inventario

"""
Un sistema de inventario muestra el estado de un producto según su stock: 0 es "Sin stock", de 1
a 5 es "Stock bajo" y más de 5 es "Stock normal". Si la cantidad es negativa, es un error de carga.

"""

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_producto = int(input("Ingrese la cantidad de productos: "))

if cantidad_producto == 0:
    print(f"Del producto {nombre_producto} no hay mas stock.")
elif cantidad_producto >= 1 and cantidad_producto <= 5:
    print(f"Del producto {nombre_producto} hay bajo stock")
elif cantidad_producto > 5:
    print(f"Del producto {nombre_producto} hay stock normal")
else:
    print("Error de carga")