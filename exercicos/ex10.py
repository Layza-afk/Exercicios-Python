#Conversor de temperatura

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