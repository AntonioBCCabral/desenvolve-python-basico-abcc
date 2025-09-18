# Criar uma lista com 20 elementos aleatórios, entre -10 e 10.
import random
lista_aleatoria = [random.randint(-10, 10) for _ in range(20)]
print("Agora, vamos ver como ficou a Lista aleatória:", lista_aleatoria)

# Descobrir a maior sequência de números negativos consecutivos na lista. Criar uma lista com essa sequência.
max_seq = []
current_seq = []
for num in lista_aleatoria:
    if num < 0:
        current_seq.append(num)
        if len(current_seq) > len(max_seq):
            max_seq = current_seq[:]
    else:
        current_seq = []
print("Maior sequência de números negativos consecutivos:", max_seq)

# Usar o comando del para remover a maior sequência negativa da lista original.
if max_seq:
    start_index = lista_aleatoria.index(max_seq[0])
    del lista_aleatoria[start_index:start_index + len(max_seq)]
print("Lista após remover a maior sequência negativa:", lista_aleatoria)


