# Estadísticas de usuarios

"""
Una app registra las edades de sus usuarios. Se ingresan una por una hasta que se escribe 0.
Muestra cuántos usuarios hay, el promedio de edad y la edad más alta.
"""

contador_usuarios = 0
sum_edad = 0
edad_mayor = 0
while True:

    edad = int(input("Ingrese su edad: "))
    if edad == 0:
        print("Proceso finalizado")
        break
    elif edad > 0:
        contador_usuarios += 1
        sum_edad += edad
        if edad > edad_mayor:
            edad_mayor = edad
    else:
        print("Debe ingresar una edad valida")
if sum_edad == 0:
    print("No hay edades para calcular su promedio")

else:
    print(f"1.Actualmente hay {contador_usuarios} usuarios.\n2.El promedio de edad es: {sum_edad / contador_usuarios:.2f}\n3.La edad mayor es: {edad_mayor} ")
