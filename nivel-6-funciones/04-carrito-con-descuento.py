#Carrito con descuento

"""
Armá una función que reciba la lista de precios de un carrito y devuelva el total. Si el total supera
$50000, aplicá 10% de descuento.
"""

def carrito_con_descuento(precios):
    total = 0
    for precio in precios:
        total += precio
    if total > 50000:
        descuento = total * 0.10
        total -= descuento

    return total

print(f"{carrito_con_descuento([25000, 25000, 25000, 25000]):.2f}")