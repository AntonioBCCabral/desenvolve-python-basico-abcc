# Entrada de dados - escolha do número "x" pelo usuário
x = int(input("Digite o número x: "))
# Enquanto "x" for menor/igual a 5, prossiguir no "loop"
while x <= 5:
    print(f"{x} não é maior do que 5")
    x = int(input("Digite o número x: "))

print(f"{x} é maior do que 5")
print("Fim")
