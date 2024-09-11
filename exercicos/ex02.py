# Encontrar um numero aleatorio

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