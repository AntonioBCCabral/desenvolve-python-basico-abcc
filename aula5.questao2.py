# Entrada de dados
idade_juliana = int(input("Qual é a idade de Juliana? "))
idade_cris = int(input("Qual é a idade de Cris? "))
# Verificar se pelo menos uma delas é maior de 17 anos
if idade_juliana > 17 or idade_cris > 17:
    print(idade_juliana > 17 or idade_cris > 17)
    print("Juliana e Cris podem entrar no bar.")
# Verificar se ambas são menores de 18 anos, ou seja, idade <= 17
else :
    print(idade_juliana > 17 and idade_cris > 17)
    print("Juliana e Cris \033[1mNÃO \033[0m" \
    "podem entrar no bar.")