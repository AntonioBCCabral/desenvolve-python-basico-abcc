# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo.
# Anagramas são palavras com os mesmos caracteres rearranjados.

# Exemplo:
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor
# Anagramas: ["amor", "mora", "ramo", "Roma"]

frase = input("Digite uma frase: ")
palavra_objetivo = input("Selecione, dentro da frase, a palavra objetivo: ")
palavras = frase.split()
anagramas = []
palavra_objetivo_ordenada = sorted(palavra_objetivo.lower())
for palavra in palavras:
    if sorted(palavra.lower()) == palavra_objetivo_ordenada:
        anagramas.append(palavra)
print(f"Anagramas: {anagramas}")
