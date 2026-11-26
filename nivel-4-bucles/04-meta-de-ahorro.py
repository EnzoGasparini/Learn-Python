# Meta de ahorro

"""
Una app de ahorro le muestra a una persona en cuántos meses llega a su meta.

Datos fijos: la persona deposita $5000 por mes, la meta es juntar $100000 y el interés es del 2% mensual.
No se pide nada por teclado.

Reglas: el saldo arranca en $0. Cada mes pasan dos cosas, en este orden:

La persona deposita los $5000.
Al total acumulado (que ya incluye ese depósito) se le suma un 2% de interés.

El proceso se repite mes a mes hasta que el saldo llegue a $100000 o lo supere.

Qué muestra: cuántos meses tardó y cuánto tiene al final.
"""
deposito = 5000
meta = 100000
saldo = 0
cantidad_meses = 0

while meta > saldo:
    saldo += deposito
    interes = saldo * 0.02
    saldo += interes
    cantidad_meses += 1


print(f"El saldo de {saldo:.2f}, se alcanzó en {cantidad_meses} meses")