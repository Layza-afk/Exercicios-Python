# 11. voce está organizando uma lista de convidados para uma festa. Crie uma lista com os numeros de 1 á 20 
# e remova todos os numeros pares, representando convidados que não podem comparecer.

convidados = list(range(1, 21))

conviImpares = []

for impar in convidados:
    if impar % 2 != 0:
        conviImpares.append(impar)

print(conviImpares)