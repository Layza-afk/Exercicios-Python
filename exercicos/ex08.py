# Calculadora Simples

print('CALCULADORA SIMPLES')

num_1 = float(input('Insira um número: '))
num_2 = float(input('Insira um outro número: '))

operador = input('Qual operador você deseja usar (+, -, *, /): ')

if operador == '+':
    soma = num_1 + num_2
    print(f'{num_1} + {num_2} = {soma}')

elif operador == '-':
    sub = num_1 - num_2
    print(f'{num_1} + {num_2} = {sub}')

elif operador == '*':
    multi = num_1 * num_2
    print(f'{num_1} + {num_2} = {multi}')

elif operador == '/':
    divi = num_1 / num_2
    print(f'{num_1} + {num_2} = {divi}')

else:
    print('tem algo de errado, tente novamente')

sair = input('Aperte ENTER para sair: ')