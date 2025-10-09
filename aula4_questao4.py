# Crie um arquivo no seu computador chamado "gabarito_forca.txt"
# com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n").
# Essas serão as opções de palavra do jogo da forca.

#import os
#palavras = input("Digite 10 palavras: ")
#caminho_palavras = os.path.join(os.getcwd(), "gabarito_forca.txt")
#with open(caminho_palavras, "w") as arquivo:
#    arquivo = palavras
#with open(caminho_palavras, "w") as arquivo_palavras:
#    for palavra in palavras.split():
#        arquivo_palavras.write(palavra + "\n")


# Escreva um programa em Python para executar o jogo, de acordo com as definições:
# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
# No início exiba o número de letras na palavra como underscores;
# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).

import os
import random

# Escolher uma palavra aleatória do arquivo gabarito_forca.txt
with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
        palavra_secreta = random.choice(palavras)
print(palavra_secreta)

with open("gabarito_enforcado.txt", "w") as arquivo:
    # Escrever o conteúdo no arquivo
    arquivo.write("\n   |---|\n       |\n       |\n       |\n ==========\n")
with open("gabarito_enforcado.txt", "r") as arquivo:
    print(arquivo.read())

def imprime_enforcado(erros):
    estagios = [
        "\n   |---|\n       |\n       |\n       |\n ==========\n",
        "\n   |---|\n   o   |\n       |\n       |\n ==========\n",
        "\n   |---|\n   o   |\n   |   |\n       |\n ==========\n",
        "\n   |---|\n   o   |\n  /|   |\n       |\n ==========\n",
        "\n   |---|\n   o   |\n  /|\\  |\n       |\n ==========\n",
        "\n   |---|\n   o   |\n  /|\\  |\n  /    |\n ==========\n",
        "\n   |---|\n   o   |\n  /|\\  |\n  / \\  |\n ==========\n"
    ]
    print(estagios[erros])
erros = 0
while erros < 6:
    print("\nA palavra secreta tem", len(palavra_secreta), "letras.")
    print("_ " * len(palavra_secreta))                          
    letra = input("Digite uma letra: ").lower()
    for i in range(len(palavra_secreta)):
        palavra_procurada = ""
        
        if letra == palavra_secreta[i]:
            print(letra, end=' ')
            palavra_procurada += letra
        
        else:
            erros += 1
            imprime_enforcado(erros)
            print("_", end=' ')
            if erros == 6:
                print("\nVocê perdeu! A palavra era:", palavra_secreta)
                break
    if palavra_procurada == palavra_secreta:
        print("\nParabéns! Você ganhou!")
        break
    print()

# OBS: Não consegui fazer o jogo funcionar corretamente, mas consegui fazer a parte
# de ler o arquivo e escolher uma palavra aleatória. Também consegui fazer a função que
# imprime o enforcado conforme o número de erros.
# Tentei várias formas de fazer o jogo funcionar, mas não consegui. De qualquer forma,
# estou enviando o que consegui fazer.
# Se possível, gostaria de receber um feedback sobre o que fiz e o que poderia melhorar.