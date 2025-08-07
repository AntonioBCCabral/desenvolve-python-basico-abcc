# Mesa de RPG - Entrada de dados
classe = input("Qual é a sua classe? (Guerreiro, Mago, Arqueiro) ")
força = int(input("Quantos pontos de força? (escolha de 1 a 20) "))
magia = int(input("Quantos pontos de magia? (escolha de 1 a 20) "))

# Verificar se a classe escolhida está consistente com os pontos atribuídos

if (classe == "Guerreiro" and força >= 15 and magia <= 10):
    print(classe == "Guerreiro" and força >= 15 and magia <= 10)

elif (classe == "Mago" and magia >= 15 and força <= 10):
    print(classe == "Mago" and magia >= 15 and força <= 10)

elif (classe == "Arqueiro" and 5 <= força <= 15 and 5 <= magia <= 15):
    print(classe == "Arqueiro" and 5 <= força <= 15 and 5 <= magia <= 15)
else:
    print(classe == "Guerreiro" and força >= 15 and magia <= 10 or classe == "Mago" and magia >= 15 and força <= 10 or 
          classe == "Arqueiro" and 5 <= força <= 15 and 5 <= magia <= 15)

if (classe == "Guerreiro" and força >= 15 and magia <= 10) or \
   (classe == "Mago" and magia >= 15 and força <= 10) or \
   (classe == "Arqueiro" and 5 <= força <= 15 and 5 <= magia <= 15):
    print("Você está apto a jogar com a classe escolhida!")
else:
    print("Você \033[1mNÃO\033[0m está apto a jogar com a classe escolhida.")