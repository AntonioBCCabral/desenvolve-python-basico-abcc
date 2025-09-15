# Gerar um valor aleatório entre 5 e 20 e armazenar em uma variável.
import random

lista1 = [random.randint(0, 50) for i in range(10)]
lista2 = [random.randint(0, 50) for i in range(10)]
print(f'A Lista 1 é: {lista1}')
print(f'A Lista 2 é: {lista2}')

# Criar uma lista com a interseção das duas listas criadas. Usando duas técnicas (funções) diferentes.
interseccao1 = list(set(lista1) & set(lista2))
print(f"A interseção1 das duas listas é: ", interseccao1)

interseccao2 = list(filter(lambda x: x in lista1, lista2))
print(f"A interseção2 das duas listas é: ", interseccao2)
print("Atenção, esta última técnica, '2', pode conter duplicatas")

# Descobrir a quantidade de elementos repetitivos da lista de interseção. Usando listas fixas.
lista_fixa_1 = [23, 23, 9, 45, 32, 50, 7, 13, 23, 32]
print(f"A Lista Fixa 1 é: {lista_fixa_1}")
lista_fixa_2 = [9, 23, 44, 49, 50, 32, 5, 18, 37, 30]
print(f"A Lista Fixa 2 é: {lista_fixa_2}")
interseccao3 = list(set(lista_fixa_1) & set(lista_fixa_2))
print(f"A interseção das duas LISTAS FIXAS é: ", interseccao3)

elemento1 = 32
ocorrencias_32_1 = lista_fixa_1.count(32)
ocorrencias_32_2 = lista_fixa_2.count(32)
print(f"O elemento {elemento1} aparece {ocorrencias_32_1} vezes na primeira e {ocorrencias_32_2} vezes na segunda.")
elemento2 = 9
ocorrencias_9_1 = lista_fixa_1.count(9)
ocorrencias_9_2 = lista_fixa_2.count(9)
print(f"O elemento {elemento2} aparece {ocorrencias_9_1} vezes na primeira e {ocorrencias_9_2} vezes na segunda")

elemento3 = 50
ocorrencias_50_1 = lista_fixa_1.count(50)
ocorrencias_50_2 = lista_fixa_2.count(50)
print(f"O elemento {elemento3} aparece {ocorrencias_50_1} vezes na primeira e {ocorrencias_50_2} vezes na segunda")

elemento4 = 23
ocorrencias_23_1 = lista_fixa_1.count(23)
ocorrencias_23_2 = lista_fixa_2.count(23)
print(f"O elemento {elemento4} aparece {ocorrencias_23_1} vezes na primeira e {ocorrencias_23_2} vezes na segunda")