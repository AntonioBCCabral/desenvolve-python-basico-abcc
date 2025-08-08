# Entrada de dados para cálculo de frete para entrega de encomendas
distancia = float(input("Digite a distância em km para entrega: "))
peso = float(input("Digite o peso da encomenda em kg: "))

# Verificar o valor do frete com base na distância e peso.
if distancia <= 100:
    if peso <= 10:
       frete = 1.00 * distancia
    else:
       frete = 1.00 * distancia + 10
elif distancia >= 101 and distancia <= 300:
    if peso <= 10:
       frete = 1.50 * distancia
    else:
       frete = 1.50 * distancia + 10
elif distancia >= 301:
    if peso <= 10:
       frete = 2.00 * distancia
    else:
       frete = 2.00 * distancia + 10

# Exibir o valor do frete
print(f"O valor do frete para entrega de uma encomenda de \033[1;32m{peso}\033[0m kg a \033[1;32m{distancia}\033[0m km \
é \033[1;36mR$ {frete:.2f}\033[0m.")


