#Carro Alugado

# Proposta: Criar uma aplicação que calcule o preço de carros alugados, levando em conta a quantidade de dias que sera alugado e o preço por dia dele.

#Instruções:
#-> Exibir um catálago de carros com seus respectivos valores por dia;
#-> Calcular e exibir ao usuario o preço que ele ira pagar no final.

carros = {
    'fiat mobi': 70,
    'fiat uno': 60,
    'fiat fiesta': 80,
    'celta': 75
}

def exibir():
    print('Catálago dos carros que podem ser alugados:')
    for nome, preco in carros.items():
        print(f'Nome: {nome} - Preço por dia: R${preco}')

exibir()

escolha = input('Qual tipo de carro você gostaria de ter (digite o nome)? ').lower()
dias = int(input('Quantos dias você gostaria de passar com o carro? '))

if escolha in carros:
    preco_total = carros[escolha] * dias
    print(f'O preço total para {dias} dias de aluguel do {escolha} é R${preco_total}.')
else:
    print('Desculpe, esse carro não está disponivel no nosso catálago ainda.')