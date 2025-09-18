# Solicitar ao usuário um número natural indefinido, a partir de 4, que será a quantidade de elementos de uma lista.
n = int(input("Digite a quantidade de elementos que deseja na lista (mínimo 4): "))
while n < 4:
    n = int(input("Por favor, digite um número maior ou igual a 4: "))

# Preencher a lista com n números, oferecidos pelo usuário.
lista_usuario = []
for i in range(n):
    numero = int(input(f"Digite o número {i+1}: "))
    lista_usuario.append(numero)
print(f"A lista criada é: {lista_usuario}")

print(f"Os 3 primeiros elementos da lista são: {lista_usuario[:3]}")
print(f"Os 2 últimos elementos da lista são: {lista_usuario[-2:]}")
print(f"Os elementos da lista em ordem inversa são: {lista_usuario[::-1]}")
print(f"Os elementos de índice par são: {[lista_usuario[i] for i in range(len(lista_usuario)) if i % 2 == 0]}")
print(f"Os elementos de índice ímpar são: {[lista_usuario[i] for i in range(len(lista_usuario)) if i % 2 != 0]}")