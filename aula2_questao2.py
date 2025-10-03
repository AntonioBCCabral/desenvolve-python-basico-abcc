# Desenvolva um programa que solicite ao usuário inserir uma frase e
# substitua todas as ocorrências de vogal por "*".
# Exemplo: Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOUáàãâéêíóôõúÁÀÃÂÉÊÍÓÔÕÚ"
frase_modificada = ""
for char in frase:
    if char in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += char
print(f"Frase modificada: {frase_modificada}")