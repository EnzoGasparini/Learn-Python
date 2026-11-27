# Carrito de compras

"""
Tienes la lista de precios de un carrito: [1200, 850, 3000, 450]. Muestra el total, el producto más
caro y el más barato.
"""
carrito_compras = [1200, 850, 3000, 450]

total_productos = 0
producto_mas_caro = 0
producto_mas_barato = carrito_compras[0]

for i in range(len(carrito_compras)):
    total_productos += carrito_compras[i]
    if producto_mas_caro < carrito_compras[i]:
        producto_mas_caro = carrito_compras[i]
    elif producto_mas_barato > carrito_compras[i]:
        producto_mas_barato = carrito_compras[i]

print(f"Total de precios: {total_productos}")
print(f"El producto más caro es de: ${producto_mas_caro}")
print(f"El producto más barato es de: ${producto_mas_barato}")