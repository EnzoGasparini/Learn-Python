# Liquidación

"""
Un producto cuesta $12000 y tiene 15% de descuento.
Mostrá cuánto se paga y cuánto se ahorra.
"""

precio_producto = int(input("Ingrese el precio del producto: "))
descuento = precio_producto * 0.15
precio_final = precio_producto - descuento

print(f"El precio final es: {precio_final:.0f}, y lo que se ahorra es: {descuento:.0f}")
