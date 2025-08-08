# Entrada de dados (dois números, para saber se a soma é par ou ímpar)
a = int(input("Digite o número 'a': "))
b = int(input("Digite o número 'b': "))
# Verificar se a soma é par ou ímpar
if (a + b) % 2 == 0:
    print(f"A soma de {a} e {b} é \033[1;32mPAR\033[0m.")
else:
    print(f"A soma de {a} e {b} é \033[1;31mÍMPAR\033[0m.")