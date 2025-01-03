# BUSCA SEQUENCIAL

def buscaSequencia(lista, valor): # Como nome já informa. Uma função que cuida de 
    for item in lista:            # encontrar um valor dentro de uma lista utilizando 
        if item == valor:         # da comparação até o encontrar.
            return True
    return False 

lista = [1, 5, 10, 15, 20, 30, 40, 50]

valor = buscaSequencia(lista, 30)

print(valor)