# Armado de cajas
"""
Un depósito empaqueta sus productos en cajas de 12 unidades. La persona ingresa cuántos
productos hay. Muestra cuántas cajas completas se arman y cuántos productos quedan sueltos.
"""

cantidad_de_productos = int(input("Ingrese la cantidad de productos: "))
cajas = cantidad_de_productos // 12
sobrantes = cantidad_de_productos % 12

print(f"{cantidad_de_productos} productos: {cajas} cajas completas y {sobrantes} productos sueltos")

