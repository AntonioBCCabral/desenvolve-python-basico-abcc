# Entrada de dados para avaliação de filmes, de 1 a 5
nota = int(input("Que nota você dá ao filme? (notas de 1 a 5, sendo '1' RUIM e '5' EXCELENTE): "))

# Verificar a nota e imprimir o resultado
if nota == 1:
    print("Você deu a nota \033[1;31m1\033[0m, para você o filme é \033[1;31mRUIM\033[0m.")
elif nota == 2:
    print("Você deu a nota \033[1;33m2\033[0m, para você o filme é \033[1;33mREGULAR\033[0m.")
elif nota == 3:
    print("Você deu a nota \033[1;34m3\033[0m, para você o filme é \033[1;34mBOM\033[0m.")
elif nota == 4:
    print("Você deu a nota \033[1;35m4\033[0m, para você o filme é \033[1;35mÓTIMO\033[0m.")
elif nota == 5:
    print("Você deu a nota \033[1;36m5\033[0m, para você o filme é \033[1;36mEXCELENTE\033[0m.")
print("Obrigado por avaliar o filme!")    
