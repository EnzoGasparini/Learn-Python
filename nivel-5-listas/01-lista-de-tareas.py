# Lista de tareas

"""
Una app de tareas pide tareas una por una hasta que la persona escribe "fin". Después muestra la
lista numerada y cuántas tareas hay.
"""
contador_tareas = 0
listas_tareas = []
while True:
    agregar_tarea = input("Introduzca la tarea que desea agregar a la lista: ")
    if agregar_tarea.lower() == "fin":
        break
    else:
        listas_tareas.append(agregar_tarea)
        contador_tareas += 1
        print(f"{contador_tareas}.{agregar_tarea} agregada exitosamente")
for i in range(contador_tareas):
    print(f"{i+1}.{listas_tareas[i]}")
print(f"En total hay {contador_tareas} tareas pendientes")