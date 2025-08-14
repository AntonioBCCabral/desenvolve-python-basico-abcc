# ATENÇÃO: vou inverter o raciocínio da questão, colocando "enquanto n >= cont". Faz mais sentido.
# Entrada de dados. O usuário escolhe o número "n".
n = int(input("Digite o número n: "))
cont = 0
# Enquanto "n" for maior ou igual ao contador, prosseguir no loop.
while n >= cont:
    print("n é maior ou igual ao contador")
    cont = cont + 1
    print(f"Agora o contador é {cont}")
    n = int(input("Digite o número n: "))

print(f"O contador agora é {cont}")
print(f"{n} é menor do que {cont}")
print("Fim")