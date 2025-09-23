# Convertendo graus Fahrenheit para Celsius.
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"A temperatura de {fahrenheit}°F equivale a {int(celsius)}°C.")
# Convertendo graus Celsius para Fahrenheit.
celsius = int(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura de {celsius}°C equivale a {int(fahrenheit)}°F.")