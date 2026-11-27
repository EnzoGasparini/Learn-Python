# Precio final

"""
Arma una función que reciba un precio y un porcentaje de descuento y devuelva cuánto hay que
pagar. Úsala con tres productos distintos.
"""
def pago_total(precio, porcentaje):
    descuento = precio * porcentaje / 100
    precio_final = precio - descuento
    return precio_final





print(f"Hay que pagar {pago_total(15000, 10):.2f}")

print(f"Hay que pagar {pago_total(76000, 40):.2f}")

print(f"Hay que pagar {pago_total(1800000, 5):.2f}")
