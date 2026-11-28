# Cajero con menu

"""
Armá un cajero con un saldo inicial de $10000 y un menú que se repite hasta que la persona elija salir.

Menú: 1) consultar saldo, 2) depositar, 3) retirar, 4) salir.

Datos que pedís: la opción y, si elige depositar o retirar, el monto.

Reglas:

Cada opción va en su propia función.
No se puede depositar ni retirar un monto de 0 o negativo: mostrá "Monto inválido".
No se puede retirar más de lo que hay: mostrá "Saldo insuficiente".
El saldo se actualiza en cada operación y se mantiene en las vueltas siguientes del menú.
"""


def consultar(saldo):
    return saldo


def depositar(saldo):
    return saldo + saldo_inicial


def retirar(saldo):
    return saldo_inicial - saldo


saldo_inicial = 10000
while True:

    eleccion_menu = int(input("Elija la operacion que desea realizar:\n1.Consultar\n2.Depositar\n3.Retirar\n4.Salir\n"))
    if eleccion_menu == 1:
        print(f"Su saldo es {consultar(saldo_inicial)}")
    elif eleccion_menu == 2:
        deposito = float(input("Introduzca el monto que desea depositar:"))
        if deposito <= 0:
            print("Monto inválido")
            continue
        print(f"Deposito: {deposito} realizado con éxito")
        deposito = depositar(deposito)
        saldo_inicial = deposito
    elif eleccion_menu == 3:
        retiro = float(input("Introduzca el monto que desea retirar:"))
        if retiro > saldo_inicial:
            print("Saldo insuficiente")
            continue
        if retiro <= 0:
            print("Monto inválido")
            continue
        print(f"Retiro: {retiro} realizado con éxito")
        retiro = retirar(retiro)
        saldo_inicial = retiro
    elif eleccion_menu == 4:
        break
    else:
        print("Opción inválida")
