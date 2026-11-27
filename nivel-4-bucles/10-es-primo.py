# Es primo ?

"""
Pedí un número entero y determina si es primo. Un número primo es mayor que 1 y solo tiene dos divisores positivos: 1 y él mismo.

Mostrá un mensaje indicando si el número ingresado es primo o no.

"""

numero_usuario = int(input("Ingrese su número: "))
es_primo = numero_usuario > 1

for i in range(2, numero_usuario):
    if numero_usuario % i == 0:
        es_primo = False
        break

if es_primo:
    print("Es primo")
else:
    print("No es primo")
