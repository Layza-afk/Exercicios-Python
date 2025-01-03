# BUSCA BINARIA

lista = [10, 15, 60, 95]

# O método de busca binaria é mais eficiente em relação ao sequêncial.
def buscaBinaria(lista, valor):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            print(f'Indice: {meio} Valor: {lista[meio]}')
            return
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    print('Valor não encontrado na lista')

buscaBinaria(lista, 95)