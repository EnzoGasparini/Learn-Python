# Mini tienda

"""
Armá una mini tienda con listas de nombres y precios de 4 productos. Un menú permite: 1) ver
productos, 2) agregar un producto al carrito (por número), 3) ver el total del carrito, 4) salir. Si el
total supera $50000, aplicá 10% de descuento. Es el ejercicio final: usa funciones, listas, bucles y
condicionales.
"""


def menu():
    print("1. Ver productos")
    print("2. Agregar productos al carrito")
    print("3. Ver el total del carrito")
    print("4. Salir")
    print("")


def ver_productos(lista1, lista2):
    for i in range(len(lista1)):
        print(f"{i + 1}.{lista1[i]}, Precio: ${lista2[i]}")
    print("")


def agregar_productos(lista1, lista2):
    ver_productos(lista1, lista2)
    opcion_usuario = int(input("Seleccione el producto que desea agregar al carrito: "))
    if opcion_usuario - 1 in range(len(lista1)):
        carrito_productos.append(lista1[opcion_usuario -1])
        carrito_precios.append(lista2[opcion_usuario - 1])
    else:
        print("Opción invalida")


def total_carritos(lista1, lista2):
    sum_total = 0
    for i in range(len(lista1)):
        print(f"{i + 1}.{lista1[i]}, Precio: ${lista2[i]}")
        sum_total += int(lista2[i])
    if sum_total > 50000:
        descuento = sum_total * 0.10
        sum_total -= descuento
        print(f"Aplica un descuento de {descuento:.2f} ")
    print(f"Total a pagar: ${sum_total:.2f}")
    print("")


carrito_productos = []
carrito_precios = []
lista_productos = ["Chocolate", "Cereales", "Leche", "Pan"]
lista_precios = [15, 8, 3, 4]
lista_prod_tecno = ["Computadora", "Mouse", "Monitor", "Silla"]
lista_precios_tecno = [35000, 3500, 27000, 12000]

while True:
    menu()
    opcion_menu = int(input("Seleccione una opcion para continuar: "))
    if opcion_menu == 4:
        break
    if opcion_menu == 1:
        ver_productos(lista_prod_tecno, lista_precios_tecno)
    elif opcion_menu == 2:
        agregar_productos(lista_prod_tecno, lista_precios_tecno)
    elif opcion_menu == 3:
        total_carritos(carrito_productos, carrito_precios)
    else:
        print("Opción invalida")
        continue
