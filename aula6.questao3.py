# Entrada de dados. Saber se o ano é bissexto ou não.
ano = int(input("Digite um ano para verificar se é bissexto: "))
a = ano % 4
b = ano % 100
c = ano % 400

# Execução dos comandos para verificar se o ano é bissexto
if (a == 0 and b != 0 or b == 0 and c == 0):
    print(f"O ano \033[1;32m{ano}\033[0m é \033[1;36mBissexto\033[0m.")
else:
    print(f"O ano \033[1;32m{ano}\033[0m \033[1mnão é Bissexto \033[0m.")