# Compra en coutas

"""
Una tienda online permite pagar en cuotas con un recargo fijo del 20%. La persona ingresa el precio del producto y la cantidad de cuotas.
Muestra el total a pagar y el valor de cada cuota.
"""

precio_producto = int(input("Ingrese el precio del producto: "))
catidad_coutas = int(input("Elija la cantidad de cuotas: "))
print("Recuerde que el pago en coutas tiene un recargo del 20%")
recargo = precio_producto * 0.20
precio_final_producto = precio_producto + recargo

print(f"Total a pagar: {int(precio_final_producto)} en 6 cuotas de: {int(precio_final_producto/catidad_coutas)}")


