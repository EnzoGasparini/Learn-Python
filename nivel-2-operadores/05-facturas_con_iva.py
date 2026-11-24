# Facturas con iva

"""
Un sistema de facturación recibe el precio de un producto sin IVA y la cantidad de unidades. El
IVA es 21%. Mostrá el subtotal, el IVA y el total.
"""

precio_producto = float(input("Ingrese el precio de un producto: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))
subtotal = precio_producto * cantidad
iva = subtotal * 0.21
total = subtotal + iva

print(f"Subtotal: {subtotal:.2f}, IVA: {iva:.2f}, Total: {total:.2f}")