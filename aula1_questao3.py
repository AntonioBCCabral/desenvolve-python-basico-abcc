# Escreva um script que, dada uma frase, conta os seus espaços em branco.
# Exemplo:
# Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
# Espaços em branco: 11


frase = input("Digite uma frase: ")
contador_espacos = frase.count(" ")
print(f"Espaços em branco1: {contador_espacos}")

# Outra forma de fazer:
contador_espacos2 = 0
for caractere in frase:
    if caractere == " ":
       contador_espacos2 += 1
print(f"Espaços em branco2: {contador_espacos2}")