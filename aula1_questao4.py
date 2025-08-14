# Entrada de dados. Comparação do numero "n" com o número "x".
n = int(input("Digite o número 'n': "))
maior = 0
if n <= 0:
    print(f"O maior é {maior}")
else:
    while n > 0:
        x = int(input("Digite o número 'x': "))
        if x > maior:
            maior = x
            n = n-1
            print(f"'n' agora vale {n}")
            print(f"O maior agora vale {maior}")
        else:
            n = n-1
            print(f"'n' agora vale {n}")
            print(f"O maior continua valendo {maior}")
    print(f"O atual maior é {maior}")    
        
    