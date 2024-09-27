#Contador de vogais

def conta_vogais(palavra):
    vogais = "aeiou"
    contador = 0

    for letra in palavra.lower():
        if letra in vogais:
            contador += 1

    return f'Palavra: {palavra}\nNumero de vogais: {contador}'

palavra = input('Digite uma palavra: ')

print(conta_vogais(palavra))

sair = input('Aperte ENTER para sair: ')