# Entrada de dados. O usuário deverá advinhar um número entre 1 e 10.
import random
numero_aleatorio = random.randint(1, 10)
#numero_aleatorio = 7
while True:
    num = int(input("Digite um número inteiro entre 1 e 10: "))
# Verificação se o número digitado é igual ao número aleatório.
    if num == numero_aleatorio:
        print("Parabéns! Você acertou o número.")
        break
    if num < 1 or num > 10:
        print("Número inválido! Tente novamente.")
        continue    
    if num <= numero_aleatorio:
        print("O número é maior.Tente novamente.")
        continue
    if num >= numero_aleatorio:
        print("O número é menor.Tente novamente.")
        continue

# Fim do código.