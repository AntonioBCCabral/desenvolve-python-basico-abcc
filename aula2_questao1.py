# Gerar 20 números aleatórios entre -100 e 100
import random
#for i in range(20):
#    numero_aleatorio = random.randint(-100, 100)
#    print(numero_aleatorio, end=' ')

# Armazenar 20 números aleatórios em uma lista e imprimir a lista
num_aleat = [random.randint(-100, 100) for i in range(20)]
print(num_aleat)

# Imprimir a lista ordenada, sem modificar a lista original
print(sorted(num_aleat))

#Imprimir a lista original
print(num_aleat)

print(max(num_aleat))
print(min(num_aleat))
print(num_aleat.index(max(num_aleat)))
print(num_aleat.index(min(num_aleat)))