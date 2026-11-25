# Estacionamiento

"""
Datos que pedís: los minutos que estuvo el auto (número entero) y si es socio (1 sí, 2 no). Supón que no pasa de un día.

Reglas:

Se cobra $1500 por hora iniciada: de 1 a 60 minutos es 1 hora, de 61 a 120 son 2 horas, de 121 a 180 son 3, y así.
El precio nunca supera los $12000 (tope).
Si es socio, se le descuenta 20% después de aplicar el tope.

Qué muestra: cuánto paga.
"""

minutos_estacionado = int(input("Ingrese los minutos que estuvo estacionado: "))
es_socio = int(input("Es socio del estacionamiento? \n1.Si\n2.No\n"))

horas = minutos_estacionado // 60
resto = minutos_estacionado % 60
if resto > 0:
    horas += 1

total_a_pagar = horas * 1500

if total_a_pagar >= 12000:
    total_a_pagar = 12000

if es_socio == 1:
    descuento_socio = total_a_pagar * 0.20
    precio_final = total_a_pagar - descuento_socio
    print(f"El total a pagar es: ${precio_final}")
elif es_socio == 2:
    print(f"El total a pagar es: ${total_a_pagar}")
else:
    print("Debe ingresar un numero valido")