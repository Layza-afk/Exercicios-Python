#Multa para altas velocidades

velocidade = float(input('Digite sua velocidade atingida: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite permitido de 80 km. Multa: {multa}')
    
elif velocidade <= 0:
    print('Ta precisando de um guincho? ligue para: 0800 123 4567')
        
else:
    print('Ta liberado')