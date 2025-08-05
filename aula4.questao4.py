valor_inserido = int(input("Digite o valor a ser inserido: R$ "))
cedulas_100 = valor_inserido // 100
cedulas_50 = (valor_inserido % 100) // 50
cedulas_20 = (valor_inserido - (cedulas_100 * 100 + cedulas_50 * 50)) // 20
cedulas_10 = (valor_inserido - (cedulas_100 * 100 + cedulas_50 * 50 + cedulas_20 * 20)) // 10
cedulas_5 = (valor_inserido - (cedulas_100 * 100 + cedulas_50 * 50 + cedulas_20 * 20 + cedulas_10 * 10)) // 5
cedulas_2 = (valor_inserido - (cedulas_100 * 100 + cedulas_50 * 50 + cedulas_20 * 20 + cedulas_10 * 10 + cedulas_5 * 5)) // 2
moedas_1 = valor_inserido - (cedulas_100 * 100 + cedulas_50 * 50 + cedulas_20 * 20 + cedulas_10 * 10 + cedulas_5 * 5 + cedulas_2 * 2)
print(f"\033[1m{cedulas_100} \033[3m Nota(s) de R$ 100 \033[0m")
print(f"\033[1m{cedulas_50} \033[3m Nota(s) de R$ 50 \033[0m")
print(f"\033[1m{cedulas_20} \033[3m Nota(s) de R$ 20 \033[0m")
print(f"\033[1m{cedulas_10} \033[3m Nota(s) de R$ 10 \033[0m")
print(f"\033[1m{cedulas_5} \033[3m Nota(s) de R$ 5 \033[0m")
print(f"\033[1m{cedulas_2} \033[3m Nota(s) de R$ 2 \033[0m")
print(f"\033[1m{moedas_1} \033[3m Moeda de R$ 1 \033[0m")
print("\033[3mObrigado por utilizar nosso sistema de troco!\033[0m")