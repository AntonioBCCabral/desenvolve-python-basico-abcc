# Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida
# atende todos os seguintes critérios:
# . Pelo menos 8 caracteres de comprimento.
# . Contém pelo menos uma letra maiúscula e uma letra minúscula.
# . Contém pelo menos um número.
# . Contém pelo menos um caractere especial (por exemplo, @, #, $).

# Exemplo: def validador_senha(senha):
# senha1 = "Senha123@"
# senha2 = "senhafraca"
# senha3 = "Senha_fraca"
# print(validador_senha(senha1))  # Saída esperada: True
# print(validador_senha(senha2))  # Saída esperada: False
# print(validador_senha(senha3))  # Saída esperada: False

import string

def validador_senha(senha):
    if len(senha) < 8:
        return False
    print("A senha deve ter pelo menos 8 caracteres.")
    if not any(char.islower() for char in senha):
        return False
    print("A senha deve conter pelo menos uma letra minúscula.")
    if not any(char.isupper() for char in senha):
        return False
    print("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(char.isdigit() for char in senha):
        return False
    print("A senha deve conter pelo menos um número.")
    if not any(char in string.punctuation for char in senha):
        return False
    print("A senha deve conter pelo menos um caractere especial.")
    return True
senha = input("Digite a senha a ser validada: ")
if not validador_senha(senha):
    print("""Senha \033[1;31mINVÁLIDA\033[0m. A SENHA DEVE TER: \
    \n. Pelo menos 8 caracteres de comprimento. \
    \n. Pelo menos uma letra maiúscula e uma letra minúscula. \
    \n. Pelo menos um número. \
    \n. Pelo menos um caractere especial (por exemplo, @, #, $).""")
else: print("Senha \033[1;32mVÁLIDA\033[0m.")
