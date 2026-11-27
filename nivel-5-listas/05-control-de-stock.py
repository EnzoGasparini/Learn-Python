#Control de stock

"""
Una tienda guarda dos listas: los productos ["mouse", "teclado", "monitor"] y su stock [10, 0, 4]. La
persona escribe un producto y le decís cuántas unidades hay. Avisa si no hay stock o si el
producto no existe.
"""

productos = ["mouse", "teclado", "monitor", "Pad", "Soporte"]
stock = [10, 4, 8, 0, 7]
consulta_producto = input("Ingrese producto: ")
for i in range(len(productos)):
    if productos[i].lower() == consulta_producto.lower():
        if stock[i] == 0:
            print(f"Del producto {productos[i]}, no hay stock")

        else:
              print(f"El producto es {productos[i]} y su stock es {stock[i]}")
        exit()

print("El producto no existe")