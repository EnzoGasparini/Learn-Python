# Costo de envío

"""
Una empresa calcula el costo de envío según el destino del paquete:

Local: $2000
Nacional: $5000
Internacional: $12000

Pedí el destino y el peso del paquete en kilogramos.
Si pesa más de 10 kg, suma un recargo de $3000. Al final, muestra el costo total del envío.
"""

destino = input("Ingrese el destino:\n"
                "1. Local\n"
                "2. Nacional\n"
                "3. Internacional\n"
                "Opción: ")
if destino == "1":
    costo = 2000
elif destino == "2":
    costo = 5000
elif destino == "3":
    costo = 12000
else:
    print("Destino invalidó")
    exit()

peso = float(input("Ingrese el peso del paquete: "))

if peso > 10:
    costo += 3000

print(f"El costo total de envió es: ${costo}")
