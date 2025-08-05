# Calculando a área do terreno.
largura = float(input("Digite a largura do terreno, em metros: "))
comprimento = float(input("Digite o comprimento do terreno, em metros: "))
area = largura * comprimento
# Calculando o preço do terreno.
metro_quadrado = float(input("Digite o valor do metro quadrado: "))
preco = area * metro_quadrado
# Exibindo os resultados.
print(f"A área do terreno é de {area:.2f} m² e o preço é de R$ {preco:,.2f}.")