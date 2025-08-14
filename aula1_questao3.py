# Entrada de dados. Vamos obter a média aritmética das notas de três matérias.
n1 = int(input("Digite a nota da Disciplina 1 (de 0 a 100) "))
n2 = int(input("Digite a nota da Disciplina 2 (de 0 a 100) "))
n3 = int(input("Digite a nota da Disciplina 3 (de 0 a 100) "))

# Obtendo a média aritmética das notas.
m = (n1 + n2 + n3) / 3
print(f"Nota da Disciplina 1 = {n1}")
print(f"Nota da Disciplina 2 = {n2}")
print(f"Nota da Disciplina 3 = {n3}")
print(f"A média final do aluno é = {m: .2f}")

# Verificando se o aluno foi aprovado, reprovado ou foi para a recuperação.
if 0 <= m < 40:
    print("Reprovado")
    print("Fim")
elif 40<= m < 60:
    print("Recuperação")
    print("Fim")
elif 60 <= m <= 100:
    print("Aprovado")
    print("Fim")
else:
    print("Média inválida. Refaça os cálculos")

