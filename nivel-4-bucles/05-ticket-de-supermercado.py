# Ticket de supermercado

"""
Ticket del supermercado

Una caja registradora suma los productos de una compra.

Datos que pedís: el precio de cada producto, uno por uno. Cuando el cajero escribe fin en lugar de un precio, la compra termina.

Qué muestra: cuántos productos se cargaron y el total a pagar.

Ejemplo: el cajero escribe 1200, 850, 3000 y después fin. Se muestran 3 productos y un total de $5050.
"""
contador = 0
total = 0

while True:
    inicio = input("Ingrese el monto del producto: ")
    if inicio.lower() == "fin":
        break
    contador += 1
    total += float(inicio)
    print(f"Producto {contador}, $ {inicio}, Total: {total:.2f}")

print(f"Está llevando {contador} productos, el monto final es: {total:.2f}")
