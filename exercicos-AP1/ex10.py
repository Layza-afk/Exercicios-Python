#Conversor de temperatura
# Nome: Conversor de temperatura.
#Proposta: Criar um programa que converte temperaturas de Celsius para Fahrenheit e vice-versa.

#Instruções:
#-> O usuário deve escolher entre converter de Celsius para Fahrenheit ou de Fahrenheit para Celsius;
#-> O programa deve solicitar a temperatura e fazer a conversão correta;
#-> Exiba o resultado.

#Fórmulas:
#-> Celsius para Fahrenheit: (C \* 9/5) + 32
#-> Fahrenheit para Celsius: (F - 32) \* 5/9

def converter():
    escolha = input('Digite C para converter de Celsius para Fahrenheit ou F para converter de Fahrenheit para Celsius: ').upper()

    if escolha == 'C':
        c = float(input('Dgite a temperatura em Celsius:' ))
        result_F = (c * 9/5) + 32
        return f'{c}°C = {result_F}F'
    elif escolha == 'F':
        f = float(input('Digite a temperatura em Fahrenheit: '))
        result_c = (f - 32) * 5/9
        return f'{f}F = {result_c}°C'
    
print(converter())