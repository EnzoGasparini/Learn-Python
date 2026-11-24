# Cuenta del restaurante.

"""
Cuatro amigos cenan y la cuenta es de $48600. Quieren dejar 10% de propina y repartir todo en partes
iguales. Mostrá cuánto paga cada uno.
"""

cantidad_amigos = int(input("Ingrese la cantidad de comensales: "))
total_cuenta = int(input("Ingrese el valor total de la comida: "))
propina = total_cuenta * 0.10
total_por_persona = (total_cuenta + propina) / cantidad_amigos
print(int(total_por_persona))
