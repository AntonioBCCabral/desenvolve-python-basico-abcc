# Exercício 4: Concatenar duas listas
from itertools import zip_longest

# O usuário deverá gerar duas listas, ainda que com quantidade de elementos diferentes
num_elementos_1 = int(input("Digite a quantidade de elementos da Lista 1: "))
# Gerando a Lista 1
lista1 = []
for i in range(num_elementos_1):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    lista1.append(elemento)
print("A Lista 1 é:", lista1)

# Gerando a Lista 2
num_elementos_2 = int(input("Digite a quantidade de elementos da Lista 2: "))
lista2 = []
for i in range(num_elementos_2):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    lista2.append(elemento)
print("A Lista 2 é:", lista2)

resultado = [item for pair in zip_longest(lista1, lista2, fillvalue=None) 
            for item in pair if item is not None]
print("A lista concatenada é:", resultado)


