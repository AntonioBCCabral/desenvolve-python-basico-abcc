# Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo
# "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos,
# e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

# Exemplo: Bom
# dia
# meu
# nome
# é
# Davi

import os
import re
caminho_arquivo_frase = os.path.join(os.getcwd(), "frase.txt")
caminho_arquivo_palavras = os.path.join(os.getcwd(), "palavras.txt")
with open(caminho_arquivo_frase, "r") as arquivo_frase:
    conteudo = arquivo_frase.read()
    palavras = re.findall(r'\b\w+\b', conteudo)
with open(caminho_arquivo_palavras, "w") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")
with open(caminho_arquivo_palavras, "r") as arquivo_palavras:
    print(arquivo_palavras.read())
print("Palavras salvas em", caminho_arquivo_palavras)