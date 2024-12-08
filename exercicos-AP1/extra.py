# Multiplos
# Proposta: Escrever um programa que imprime os números de 1 a 100 e a cada numero q seja multimo de 3 e 5 ou so de um deles, mostrar no formato simplificado.

#Instruções:
#-> Para múltiplos de 3, imprima o numero no formato de potência, exemplo: o numero era 9, impirmir 3\*3;
#-> Para múltiplos de 5, mesma coisa. Imprimir o numero no seu formato simplificado;
#-> Para múltiplos de 3 e 5, impirmir ambas formas de simplificação.

def multiplos():
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print(f'3 * {i/3} ou 5 * {i/5}')
        elif i % 3 == 0:
            print(f'3 * {i/3}')
        elif i % 5 == 0:
            print(f'5 * {i/5}')
        else:
            print(i)

print(multiplos())