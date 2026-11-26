#Tabla del prestamo

"""
Una app de préstamos le muestra al cliente cómo va bajando su deuda mes a mes.

Datos que pedís: el monto del préstamo y la cantidad de cuotas.

Reglas:

Todas las cuotas valen lo mismo y no hay intereses, así que cada cuota es el monto dividido la cantidad de cuotas.
Cada mes la persona paga una cuota y la deuda baja en ese valor.

Qué muestra: una línea por cada mes, con el número de mes, lo que paga ese mes y lo que todavía debe después de pagar. En el último mes la deuda tiene que quedar en 0.
"""

monto_prestamo = int(input("Introduce tu monto: "))
cantidad_cuotas = int(input("Introduce tu cantidad de cuotas: "))
total_cuotas = monto_prestamo / cantidad_cuotas

for i in range(1, cantidad_cuotas + 1):
    monto_prestamo -= total_cuotas
    print(f"Mes {i} abona ${total_cuotas:.2f}, falta pagar {monto_prestamo:.2f}")