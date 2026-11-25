#Entrada de cine

"""
Un cine cobra $6000 la entrada general. Los menores de 12(inclusive) años y los mayores de 65(inclusive) pagan la
mitad. Los miércoles todas las entradas tienen 20% de descuento. Pedí la edad y el día, y muestra
el precio de la entrada.
"""

edad = int(input("Ingrese su edad: "))
dia = input("Ingrese el dia de la función: ")


if edad <= 12 or edad >= 65:
    entrada = 6000 // 2
else:
    entrada = 6000

if dia == "Miercoles" or dia == "miercoles" or dia == "MIERCOLES":
    descuento_veinte = entrada * 0.20
    total_a_pagar =  entrada - descuento_veinte
else:
    total_a_pagar = entrada
print(f"El total a pagar es {total_a_pagar}")
