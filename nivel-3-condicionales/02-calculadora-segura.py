# Calculadora segura

"""
Una calculadora pide dos números y una operación (+, -, *, /) y muestra el resultado.
Si la operación no existe o se intenta dividir por cero, avisa con un mensaje.
"""

print("Bienvenido a la calculadora segura.")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese el operacion: ")

resultado_calculado = True

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir por cero")
        resultado_calculado = False
    else:
        resultado = numero1 / numero2
else:
    print("Operacion no valida")
    resultado_calculado = False

if resultado_calculado:
    print("Resultado: ", resultado)
