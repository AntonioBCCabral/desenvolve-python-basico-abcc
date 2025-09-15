# Gerar um valor aleatório entre 5 e 20 e armazenar em uma variável.
import random

num_elementos = random.randint(5, 20)
print(f'Quantidade de elementos: {num_elementos}')

# Gerar uma lista com a quantidade de elementos sorteada, com valores entre 1 e 10.
elementos = [random.randint(1, 10) for i in range(num_elementos)]
print(f'Lista aleatória: {elementos}')

# Calcular a soma dos elementos da lista e a média.
soma = sum(elementos)
media = soma / num_elementos
print(f'Soma dos elementos: {soma}, Média dos elementos: {media}')