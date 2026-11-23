# Turista

"""
Un turista te dice la temperatura en Celsius.
Decile cuánto es en Fahrenheit.
"""
temperatura_celsius = float(input("Ingrese la temperatura: "))
temperatura_fahrenheit = temperatura_celsius * 1.8 + 32
print(f"La temperatura en fahrenheit es: {temperatura_fahrenheit:.1f}")