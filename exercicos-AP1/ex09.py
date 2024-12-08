#Contador de vogais
# Proposta: Escrever um programa que conte o número de vogais em uma frase fornecida pelo usuário.

#Instruções:
#-> O usuário deve inserir uma frase;
#-> O programa deve contar quantas vogais (a, e, i, o, u) existem na frase, desconsiderando maiúsculas ou minúsculas;
#-> Exiba o total de vogais ao final.

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