#votação da feira

banca = {
    'abacate': 'a',
    'morango': 'b',
    'caju': 'c',
    'uva': 'd',
    'mexirica': 'e',
    'fruta do dragão': 'f'
}

soma = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0
}

def exibir():
    print('ESCOLHA SUA FRUTA FAVORITA E A FAÇA VITORIOSA')
    for fruta, voto in banca.items():
        print(f'Fruta: {fruta} - ({voto})')

exibir()

for i in range(20):
    escolha = input('Escolha uma fruta e digite a letra respectiva a ela: ').lower()

    if escolha in banca.values():
        soma[escolha] += 1

    else: 
        print('esse voto não existe. Por favor digite letras validas.')
        escolha = input('Escolha uma fruta e digite a letra respectiva a ela: ').lower()

print('CONTAGEM DE VOTOS!!')
for fruta, voto in banca.items():
    print(f'{fruta}: {soma[voto]} votos')

sair = input('para sair, aperte em qualquer tecla: ')