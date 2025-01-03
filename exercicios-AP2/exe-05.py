# RECURSÃO

# exercicio de inverter string com recursão
def inverter(l):
    if len(l) == 0:
        return ''
    return l[-1] + inverter(l[:-1]) # Recursão: sempre que chamamos a função dentro dela mesmo

print(inverter('inverte'))