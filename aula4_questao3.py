# Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador
# com o nome "estomago.txt".
# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# . O texto das primeiras 25 linhas
# . O número de linhas do arquivo
# . A linha com maior número de caracteres
# . O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações
#   de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte
#   de outras palavras).

# abrir o arquivo estomago.txt para leitura, imprimir as primeiras 25 linhas.
import os

caminho_arquivo = os.path.join("estomago.txt")
with open(caminho_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
    print("Primeiras 25 linhas do arquivo:")
    for linha in linhas[:25]:
        print(linha, end='')

# contar o número de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\nNúmero de linhas do arquivo: {num_linhas}")

# encontrar a linha com maior número de caracteres. Imprimir essa linha.
# (na verdade é um parágrafo, porque no texto original não existe separação por linha).
    linha_mais_longa = max(linhas, key=len)
    print(f"\nLinha [parágrafo] com maior número de caracteres ({len(linha_mais_longa)} caracteres):")
    print(linha_mais_longa, end='')

# contar o número de menções aos nomes dos personagens "Nonato" e "Íria"
# (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir
# a substring "iria", ou seja o "I" ou "i" tem que ser acentuado).
    conteudo_arquivo = ''.join(linhas).lower()
    num_mencoes_nonato = conteudo_arquivo.count("Nonato".lower())
    num_mencoes_iria = conteudo_arquivo.count("Íria".lower())
    print(f"\nNúmero de menções ao personagem 'Nonato': {num_mencoes_nonato}")
    print(f"Número de menções ao personagem 'Íria': {num_mencoes_iria}")
    print(f"Número de menções ao verbo ir, no futuro do pretérito: {conteudo_arquivo.count('Iria'.lower())}")


