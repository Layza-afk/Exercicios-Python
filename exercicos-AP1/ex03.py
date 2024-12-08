#Multa para altas velocidades
# Proposta: Criar uma aplicação que receba a velocidade de um carro. Se ele ultrapassar os 80Km/h, mostre uma mensagem dizendo que ele foi multado.

#Instruções:
#-> Multa vai custar R$ 7,00 por cada km acima do limite;
#-> Exibir a multa no final.

velocidade = float(input('Digite sua velocidade atingida: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite permitido de 80 km. Multa: {multa}')
    
elif velocidade <= 0:
    print('Ta precisando de um guincho? ligue para: 0800 123 4567')
        
else:
    print('Ta liberado')