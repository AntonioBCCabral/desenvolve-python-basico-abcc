# Entrada de dados para obtenção de aposentadoria
sexo = input("Qual é o seu sexo? (M/F) ")
idade = int(input("Qual é a sua idade? "))
tempo_contribuicao = int(input("Quantos anos de contribuição você tem? "))
# Verificar se a pessoa está apta a se aposentar
if (sexo == "M" and idade >= 65 or sexo == "M" and tempo_contribuicao >= 30 or idade >= 60 and tempo_contribuicao >= 25):
    print((sexo == "M" and idade >= 65) or (sexo == "M" and tempo_contribuicao >= 30) or (idade >= 60 and tempo_contribuicao >= 25))
    print("Você está apto a se aposentar!")
elif (sexo == "F" and idade >= 60 or sexo == "F" and tempo_contribuicao >= 30 or idade >= 60 and tempo_contribuicao >= 25):
    print((sexo == "F" and idade >= 60) or (sexo == "F" and tempo_contribuicao >= 30) or \
         (idade >= 60 and tempo_contribuicao >= 25))
    print("Você está apto a se aposentar!")

else:
    print((sexo == "M" and idade >= 65) or (sexo == "M" and tempo_contribuicao >= 30) or (idade >= 60 and tempo_contribuicao >= 25) or \
          (sexo == "F" and idade >= 60) or (sexo == "F" and tempo_contribuicao >= 30) or (idade >= 60 and tempo_contribuicao >= 25))
    print("Você \033[1mNÃO\033[0m está apto a se aposentar.")