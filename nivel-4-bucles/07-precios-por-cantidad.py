# Precios por cantidad

"""
Una tienda mayorista vende un producto a $2500 por unidad. Al comprar 5 unidades o más, aplica un descuento del 5% sobre el total.

Muestra una tabla con la cantidad de unidades, el precio sin descuento y el precio final para compras de 1 a 10 unidades.
Usa el descuento solo cuando corresponda.
"""

precio_unidad = 2500
precio_total = 0

for i in range(1, 11):
    if i >= 5:
        precio_total += precio_unidad
        descuento_cinco = precio_total * 0.05
        precio_descuento = precio_total - descuento_cinco
        print(
            f"Cantidad de productos: {i}, total sin descuento: {precio_total:.2f}, aplica descuento, precio final: {precio_descuento:.2f}")

    else:
        precio_total += precio_unidad
        print(f"Cantidad de productos: {i}, total sin descuento: {precio_total:.2f}, precio final {precio_total:.2f}")
