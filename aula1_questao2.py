# Entrada de dados. Obter um número "n"
import math
import random
#n = int(input("Digite um número inteiro positivo (entre 1 e 20): "))
while True:
    n = int(input("Digite um número inteiro positivo (entre 1 e 20): "))
    if 0 < n < 21:
        soma = sum(random.randint(1, 100) for i in range(n))
        print(f"A soma dos {n} números aleatórios é: {soma}")
        raiz_quadrada = math.sqrt(soma)
        print(f"A raiz quadrada da soma é: {raiz_quadrada: .2f}")
        break
               
    else:
        print("Número inválido! Por favor, digite um número entre 1 e 20.")
        continue
            