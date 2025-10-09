# Escreva um script Python que solicita uma frase do usuário e a
# salve em um arquivo chamado "frase.txt" no mesmo local do seu script.
# Imprima em seguida o caminho completo do arquivo salvo.

# Exemplo: Digite uma frase: Bom dia, meu nome é Davi.
# Frase salva em /Users/laranjeira/python-basico/frase.txt

import os
frase = input("Digite uma frase: ")
caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(frase)
print("Frase salva em", caminho_arquivo)
