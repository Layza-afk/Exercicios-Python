# 4. Decidiu reorganizar suas tarefas começando pela última. Inverta a lista.
tarefas = list(range(1, 11))
tarefas.reverse() # método usado para inverter uma sequência

print(f'Tarefas: {tarefas}')

# 8. O primeiro cliente da fila foi atendido e saiu da loja. Remova o elemento da frente da fila
fila = []

fila.append('X') #método utilizado para add um item a uma lista
fila.append('Y')
fila.append('Z')

fila.pop(0) # método usado para remover o primeiro item colocado em uma fila

print(f'Clientes na fila: {fila}')

