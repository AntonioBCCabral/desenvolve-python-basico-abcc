# Entrada de dados: calcular a média de idade dos respondentes da pesquisa

N = int(input("Digite a quantidade de respondentes da pesquisa: N = "))
cont = 1
soma = 0

# Acumulando as idades de todos os N respondentes.
while cont <= N:
    idade = int(input("Digite, uma a uma, a idade de cada respondente: idade = "))
    soma = idade + soma
    cont += 1

# Saída de dados, tanto o acumulado quanto a média procurada.
print(f"A soma das idades de {N} respondentes da pesquisa é: {soma} ")
print(f"A média de idade dos respondentes é = {soma / N: .0f} anos.")