# Calculadora con menu

"""
Armá una calculadora con un menú: 1) sumar, 2) restar, 3) multiplicar, 4) dividir, 5) salir. Pide los
dos números, muestra el resultado y vuelve al menú hasta que la persona elija salir. Cada
operación va en su propia función.
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0 :
        return print("")
    else:
        return a / b


while True:
    eleccion_menu = int(input("Elija una operacion para realizar:\n1.Suma\n2.Resta\n3.Multiplicar\n4.Dividir\n5.Salir\n"))
    if eleccion_menu == 5 or eleccion_menu < 1 or eleccion_menu > 5:
        break
    num1 = int(input("Elija el primer numero:"))
    num2 = int(input("Elija el segundo numero:"))
    if eleccion_menu == 1:
        print(f"La suma de sus números es: {suma(num1, num2)}")
        print("")
    elif eleccion_menu == 2:
        print(f"La resta de sus números es: {resta(num1, num2)}")
        print("")
    elif eleccion_menu == 3:
        if num2 <= 0 :
            print("No se puede dividir por 0")
        else:
            print(f"La multiplicación de sus números es: {multiplicar(num1, num2)}")
            print("")
    elif eleccion_menu == 4:
        print(f"La division de sus numeros es = {dividir(num1, num2)}")
        print("")





