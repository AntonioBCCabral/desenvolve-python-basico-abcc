# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados,
# bem como a chave da criptografia. Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis
# (entre 33 e 126 na tabela Unicode)

# Exemplo:
# nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
# chave_aleatoria = 5
# nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random
nomes = input("Digite uma lista de nomes separados por um espaço: ").split(" ")
print(nomes)

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []
    for nome in nomes:
        nome_cript = ""
        for char in nome:
            char_cript = chr((ord(char) + chave_aleatoria))
            nome_cript += char_cript
        nomes_cript.append(nome_cript)
    return nomes_cript, chave_aleatoria
nomes_criptografados, chave = encrypt(nomes)
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")

