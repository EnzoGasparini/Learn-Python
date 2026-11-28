# Tarifa de estacionamiento

"""
Creá una función que reciba dos datos: los minutos que un vehículo estuvo estacionado y si su dueño es socio (`True` o `False`).
La función debe calcular y devolver el importe a pagar con estas reglas:

- Se cobran $1500 por cada hora iniciada. Por ejemplo, 61 minutos cuentan como 2 horas.
- El importe antes del descuento no puede superar los $12.000.
- Si la persona es socia, aplicá un descuento del 20% después de calcular el tope.

Usá la función con tres clientes distintos, con diferentes tiempos de estacionamiento y condición de socio, y mostrale a cada uno cuánto debe pagar.
"""

def total_estacionamiento(minutos, es_socio):

    horas_enteras = minutos // 60
    horas_decimales = minutos % 60
    horas_totales = horas_enteras
    if horas_decimales > 0:
        horas_totales += 1

    sub_total = horas_totales * 1500
    if sub_total > 12000:
        sub_total = 12000

    if es_socio:
        descuento = sub_total * 20 // 100
        sub_total -= descuento

    return sub_total

print(f"Usted debe abonar un total de: ${total_estacionamiento(120, True)}")
print(f"Usted debe abonar un total de: ${total_estacionamiento(250, False)}")
print(f"Usted debe abonar un total de: ${total_estacionamiento(61, True)}")
