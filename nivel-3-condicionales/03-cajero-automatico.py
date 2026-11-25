# Cajero automático

"""
Un cajero dispone de un saldo y solo puede entregar billetes de $100. Pedí a la persona el monto que desea retirar.
Si el monto es múltiplo de $100 y no supera el saldo disponible, descuéntalo del saldo y muestra cuánto dinero queda.
Si no se puede realizar el retiro, explica el motivo.
"""

saldo_cajero = 12000
print("Bienvenido al cajero!")
monto_retirar = int(input("Ingrese el monto que desea retirar: "))

if saldo_cajero >= monto_retirar and monto_retirar > 0 and monto_retirar % 100 == 0:
    saldo_cajero -= monto_retirar
    print(f"Operacion realizada con exito, quedan ${saldo_cajero} disponibles")
elif saldo_cajero < monto_retirar:
    print("No hay suficientes fondos")
elif monto_retirar <= 0:
    print("Debe ingresar un numero valido")
else:
    print("Lo sentimos solo contamos con billetes de 100")

