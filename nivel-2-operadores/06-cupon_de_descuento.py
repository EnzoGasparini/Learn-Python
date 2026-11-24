#Cupon de descuento

"""
Una tienda aplica 10% de descuento en todos sus productos y, sobre ese precio, un cupón extra
de 5%. Muestra el precio final y cuánto se ahorró en total.
"""

precio_producto = float(input("Ingrese el precio del producto: "))
monto_descuento_diez = precio_producto * 0.10
precio_descuento_10 = precio_producto - monto_descuento_diez
monto_descuento_cinco = precio_descuento_10 * 0.05
precio_final = precio_descuento_10 - monto_descuento_cinco

print(f"El precio final es: {precio_final:.2f} y usted ahorró en total: {(monto_descuento_diez + monto_descuento_cinco):.2f}")