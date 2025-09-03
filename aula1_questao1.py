# Entrada de dados. Dois números decimais, positivos ou negativos.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# Cálculo da soma absoluta dos números.
soma_absoluta = abs(num1) + abs(num2)
# Exibição do resultado.
print(f"A soma absoluta dos números é: {soma_absoluta}")
# Arredondando o resultado para duas casas decimais.
soma_absoluta_arredondada = round(soma_absoluta, 2)
# Exibição do resultado arredondado.
print(f"A soma absoluta dos números arredondada para duas casas decimais é: {soma_absoluta_arredondada}")

# Cálculo da diferença absoluta dos números.
diferenca_absoluta = abs(num1 - num2)
# Exibição do resultado.
print(f"A diferença absoluta dos números é:", round(diferenca_absoluta, 2))