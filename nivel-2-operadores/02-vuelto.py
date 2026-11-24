# Vuelto

"""
Tenés que devolver $4350 de vuelto con billetes de $1000, $500, $100 y $50. Mostrá cuántos billetes
de cada valor entregás, usando la menor cantidad posible.
"""
cantidad_de_vuelto = int(input("Ingrese la cantidad de vuelto: "))

cantidad_billetes_mil = cantidad_de_vuelto // 1000
resto = cantidad_de_vuelto % 1000

cantidad_billetes_quinientos = resto // 500
resto = resto % 500

cantidad_billetes_cien = resto // 100
resto = resto % 100

cantidad_billetes_cincuenta = resto // 50

print("Billetes de $1000:", cantidad_billetes_mil)
print("Billetes de $500:", cantidad_billetes_quinientos)
print("Billetes de $100:", cantidad_billetes_cien)
print("Billetes de $50:", cantidad_billetes_cincuenta)