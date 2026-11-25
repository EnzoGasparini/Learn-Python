# Tienda con socios

"""
Tienda con socios. Una tienda aplica descuentos según el total de la compra.

Datos: el total de la compra y si la persona es socia (si o no).

Reglas:

Menos de $10000: sin descuento.
De $10000 a $50000 (inclusive): 10%.
Más de $50000: 20%.
Si es socia, se le descuenta un 5% más sobre el precio que ya quedó con descuento.

Qué muestra: cuánto paga y cuánto ahorra (la compra original menos lo que paga).
"""

total_compra = float(input("Ingrese el total de la compra: "))
es_socio = int(input("Es usted socio? \n1.Si. \n2.No.\n"))

descuento_diez = total_compra * 0.10
descuento_veinte = total_compra * 0.20

if total_compra >= 10000 and total_compra <= 50000:
    precio_final = total_compra - descuento_diez

elif total_compra > 50000:
    precio_final = total_compra - descuento_veinte

else:
    precio_final = total_compra

if es_socio == 1:
    descuento_cinco = precio_final * 0.05
    total_a_pagar = precio_final - descuento_cinco
else:
    total_a_pagar = precio_final

ahorro = total_compra - total_a_pagar

print(f"El total a pagar es: {total_a_pagar:.2f} y esta ahorrando {ahorro:.2f}")
