# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
# imprima a data com o nome do mês por extenso.
# Dica: usando listas você não precisa fazer um "if" para cada mês.

# Exemplo: Digite uma data de nascimento: 29/10/1973
# Você nasceu em 29 de outubro de 1973.

data_nascimento = input("Digite uma data de nascimento no formato 'dd/mm/aaaa'): ")
dia, mes, ano = data_nascimento.split("/")
meses = ["xangonblau", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes_extenso = meses[int(mes)]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")