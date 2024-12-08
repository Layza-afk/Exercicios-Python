# Encontrar um numero aleatorio
# Proposta: Um jogo onde a maquina deve escolher um numero aleatorio de 1 a 100 e o usuario deve adivinhar qual numero é. 
# O usuario so tem 5 tentativas para acertar o numero.

# Instruções:
#-> O computador deve informa sempre a quantidade de tentativas que restam;
#-> A cada tentativa perdida, o computador deve informa uma dica ao usuario (si ta perto ou longe);
#-> So a 5 tentativas;
#-> Se conseguir adivinhar, ganha o jogo. Se não conseguiu e perdeu as tentativas, perdeu o jogo.

import random

numero_random = random.randint(1, 100)
tentativas = 5

print('----------- MINI-GAME ------------')
print('------ Encontre o numero perdido ------')

print(f'Você tem {tentativas} tentativas para tentar')
numero_user = int(input('Digite um numero: '))

while numero_user != numero_random:
    tentativas -= 1
    if numero_user > numero_random: 
        print('o numero é menor')

    elif numero_user < numero_random:
        print('O número é maior')
     
    if tentativas == 1:
        print(f'Tentativa restante: {tentativas}')
    elif tentativas == 0:
        print(f'Você perdeu, melhor!')
        break
    else:
        print(f'Tentativas restantes: {tentativas}')

    numero_user = int(input('Digite um numero novamente: '))

if numero_user == numero_random:
    print('Você acertou o número!! Um grande mestre da adivinhação')
else:
    print('Não foi dessa vez')