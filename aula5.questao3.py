# Entrada de dados
idade = int(input("Qual é a sua idade? "))
# Verificar se a pessoa tem entre 16 e 18 anos
if 16 <= idade <= 18:
    print(16 <= idade <= 18)
else:
    print(16 <= idade <= 18)
    
quantidade_jogos = int(input("Quantos jogos você já jogou? "))
# Verificar se a pessoa já jogou mais de 2 jogos
if quantidade_jogos > 2:
    print(quantidade_jogos > 2)
else:
    print(quantidade_jogos > 2)

quantidade_vitorias = int(input("Quantas vitórias você já teve? "))
# Verificar se a pessoa já teve mais de 0 vitórias
if quantidade_vitorias > 0:
    print(quantidade_vitorias > 0)
else:
    print(quantidade_vitorias > 0)

# Verificar se a pessoa pode está apta a ingressar no Clube do Tabuleiro
if (16 <= idade <= 18) and (quantidade_jogos > 2) and (quantidade_vitorias > 0):
    print("Você está apto a ingressar no Clube do Tabuleiro!")
else:
    print("Você \033[1mNÃO\033[0m está apto a ingressar no Clube do Tabuleiro.")


    