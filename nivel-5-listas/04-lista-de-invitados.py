#Lista de invitados

"""
Tenés la lista de invitados de una fiesta. Una persona dice su nombre y le decís si está invitada y,
si lo está, en qué posición figura (contando desde 1).
"""

lista_de_invitados = ["Juan","Matias","Ana","Florencia","Martin"]
nombre_del_invitado = input("Ingrese su nombre: ")
for i in range (len(lista_de_invitados)):
    if nombre_del_invitado.lower() == lista_de_invitados[i].lower():
        posicion = i + 1
        print(f"Bienvenido/a {lista_de_invitados[i]}, su ubicación es la lista es la número {posicion}")
        exit()

print("Lo sentimos no está en la lista de invitados.")
