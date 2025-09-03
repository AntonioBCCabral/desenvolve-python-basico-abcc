# Imprimir a data e a hora atual.

import datetime
data_hora_atual = datetime.datetime.now()

data = data_hora_atual.strftime('%d/%m/%Y')
print(data)

hora = "0{}:0{}".format(data_hora_atual.hour, data_hora_atual.minute, data_hora_atual.second)
print(hora)

# Fim do código.