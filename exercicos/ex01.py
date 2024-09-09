#Calcular pedidos 

tipo_clientes = {
    "PRECO": {
        "Alunos de graduação": 1.0,
        "Alunos de Pos-graduação": 2.0,
        "Funcionarios": 3.0,
        "Professor": 10.0,
        "externo": 15.0
        },
    "TIPO": {
        "Alunos de graduação": 1,
        "Alunos de Pos-graduação": 2,
        "Funcionarios": 3,
        "Professor": 4,
        "externo": 5
        }
    }

def exibir():
    print("Tipos de Clientes e seus preços para comer:")
    for tipo, preco in tipo_clientes["PRECO"].items():
        codigo = tipo_clientes["TIPO"][tipo]
        print(f'{codigo} - {tipo}: ${preco:.2f}')

print(exibir())

tipo = int(input('Digite o numero do tipo de cliente que você é: '))
quantidade = int(input('Digite a quantidade de membros do seu tipo: '))

def calculo():
    if tipo == 1:
        totalpago = quantidade * 1
        return totalpago
    elif tipo == 2:
        totalpago = quantidade * 3
        return totalpago
    elif tipo == 3:
        totalpago = quantidade * 5
        return totalpago
    elif tipo == 4:
        totalpago = quantidade * 10
        return totalpago
    elif tipo == 5:
        totalpago = quantidade * 15
        return totalpago

total_pago = calculo()
print(f'Total a ser pago: ${total_pago:.2f}')