catalago = {
    "tênis": 20.00,
    "mochila": 199.00,
    "colar": 480.00
}

descontos = {
    2: 0.05,
    3: 0.07,
    4: 0.12
}

def exibir():
    print("CATALAGO")
    for item, preco in catalago.items():
        print(f'{item}: R${preco}')
    for num, desco in descontos.items():
        print(f'na compra de {num} você tera de desconto: {desco*100}%')

exibir()

clientes = int(input('Quantos itens você gostaria de comprar? '))

if clientes in descontos:
    itens_desejados = input('Digite o nome dos itens desejados (separados por virgula): ')
    itens_escolhidos = itens_desejados.split(',')

    preco_total = sum(catalago.get(item.strip(), 0) for item in itens_escolhidos)
    preco_total_desconto = preco_total * (1 - descontos[clientes])

    print(f'Preço total sem o desconto da loja: R$ {preco_total}')
    print(f"Preço total de sua compra com desconto: R${preco_total_desconto}")

else:
    print('Para esse numero de compras não temos desconto')