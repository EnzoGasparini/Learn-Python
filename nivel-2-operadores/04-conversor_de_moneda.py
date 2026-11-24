# Conversor de moneda

"""
Una app de viajes convierte pesos a dólares. La persona ingresa cuántos pesos tiene y a cuánto
está el dólar. Muestra cuántos dólares recibe, con 2 decimales.
"""

total_a_convertir = float(input("Ingrese el monto total en Pesos que desea convertir a dólares: "))
cotizacion_dolar = 1550
print(f"La cotización del dólar es {cotizacion_dolar}")
total_convertido = total_a_convertir / cotizacion_dolar
print(f"Su cantidad en dólares es {total_convertido:.2f}")