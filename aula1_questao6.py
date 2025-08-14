# Entrada de dados. Verificar a quantidade de cobaias utilizadas e seus percentuais.

N = int(input("Digite a quantidade de experimentos realizados: "))
cont = 1
somaS = 0
somaR = 0
somaC = 0
while cont <= N:
    sapos = int(input("1 - Quantidade de sapos utilizados neste experimento: "))
    ratos = int(input("2 - Quantidade de ratos utilizados neste experimento "))
    coelhos = int(input("3 - Quantidade de coelhos utilizados neste experimento "))
    somaS = somaS + sapos
    somaR = somaR + ratos
    somaC = somaC + coelhos
    cont += 1
print(f"Foram utilizados \033[1;31m{somaS} sapos.\033[0m")
print(f"Foram utilizados \033[1;32m{somaR} ratos.\033[0m")
print(f"Foram utilizados \033[1;33m{somaC} coelhos.\033[0m")
cobaias = somaS + somaR + somaC
percentS = somaS / cobaias * 100
percentR = somaR / cobaias * 100
percentC = somaC / cobaias * 100
print(f"No total, foram utilizadas \033[1;38m{cobaias} cobaias.\033[0m")
print(f"Percentual de sapos = \033[1;35m{percentS: .2f} %\033[0m")
print(f"Percentual de ratos = \033[1;36m{percentR: .2f} %\033[0m")
print(f"Percentual de coelhos = \033[1;30m{percentC: .2f} %\033[0m")
