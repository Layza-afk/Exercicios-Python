#Quizz

import random

palavras = {
    'gato': ['É um animal', 'Costuma dormi muito, mas sempre que ta acordado ta nos 300v', 'Faz "miua"'],
    'sorvete': ['É uma bagana', 'Para uma melhor expretiencia comendo, é bom gelado', 'Pode usar casquinha ou em um copo'],
    'cadeira': ['Tu senta nela', 'Em alguns modelos ela dobra', 'é um objeto']
}

palavra, dica = random.choice(list(palavras.items()))

tentativas = 0
tentativas_max = 3

print('BEM VENDO AO JOGO DE ADIVINHÇÃO DE PALAVRAS!')

while tentativas < tentativas_max:
    print(f'\nDica {tentativas + 1}: {dica[tentativas]}')
    resposta = input('Qual é a palavra: ')

    if resposta.lower() == palavra.lower():
        print('Parabens, voce acertou a palavra.')
        break
    else:
        tentativas += 1
        if tentativas == tentativas_max:
            print(f'Você errou, Burro. A palavra era: "{palavra}"')
        else:
            print(f'Tente novamente. Numero de tentativas usadas: {tentativas}, numero de tentativas totais: {tentativas_max}')

print('FIM')

sair = input('Para sair, aperte ENTER: ')