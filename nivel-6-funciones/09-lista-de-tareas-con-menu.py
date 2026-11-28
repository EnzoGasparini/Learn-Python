# Lista de tareas con menu

"""
Una app de tareas guarda las tareas en una lista que arranca vacía y muestra un menú que se repite hasta que la persona elija salir.

Menú: 1) agregar tarea, 2) ver tareas, 3) marcar una como hecha, 4) salir.

Datos que pedís: la opción. Si agrega, el texto de la tarea. Si marca una como hecha, el número de la tarea tal como se ve en la lista (contando desde 1).

Reglas:

Cada opción va en su propia función.
Ver tareas muestra la lista numerada desde 1, o "No hay tareas" si está vacía.
Marcar como hecha elimina la tarea de la lista.
Si el número no existe, mostrá "Número inválido".
Si la opción del menú no existe, mostrá "Opción no válida".
"""
def agregar_tareas(tarea):
    tareas.append(tarea)

def ver_tareas(tareas):
    contador = 0
    print("***** Lista de Tareas *****")
    for i in tareas:
        contador += 1
        print(f"{contador}.{i}")
    print("")

def marcar_tareas(tarea):
    tareas.pop(tarea)

tareas = []

while True:
    opcion_menu = int(input("Seleccione una opcion para continuar:\n1.Agregar tareas.\n2.Mostrar tareas.\n3.Marcas tareas compleatadas.\n4.Salir.\n"))
    if opcion_menu == 4:
        break
    if opcion_menu == 1:
        tarea = (input("Introduzca la tarea que desea agregar: "))
        agregar_tareas(tarea)
    elif opcion_menu == 2:
        if len(tareas) == 0:
            print("NNo hay tareas")
            continue
        ver_tareas(tareas)
    elif opcion_menu == 3:
        if len(tareas) == 0:
            print("No hay tareas")
            continue
        ver_tareas(tareas)
        seleccion_tarea = int(input("Elija el numero de tarea que desea marcar como completa: "))
        if seleccion_tarea in range(1, len(tareas) + 1):
            print(f"La tarea {tareas[seleccion_tarea - 1]} fue completada")
            marcar_tareas(seleccion_tarea - 1)
        else:
            print("Número inválido")
    else:
        print("Opción no válida")
        continue


