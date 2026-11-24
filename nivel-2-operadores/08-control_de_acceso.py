# Control de acceso

"""
Para entrar a un evento hay que tener entrada y además tener 18 años o más o ir acompañado de un
adulto. Pedí la edad, si tiene entrada y si va acompañado ("si" o "no"). Muestra True o False según
si puede entrar.
"""

tiene_entrada = input("Tiene entrada: ")
edad = int(input("Edad: "))
viene_acompañado = input("Viene acompañdo por un adulto: ")

puede_ingresar = tiene_entrada == "si" and (edad >= 18 or viene_acompañado == "si")

print(f"Puede ingresar: {puede_ingresar}")
