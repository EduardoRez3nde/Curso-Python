velocidade = int(input('Velocidade do carro km: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade. multado!')
    print(f'Multa de R$100 mais quilometro acima do limite R${multa}')
    print(f'Total da multa: R${100 + multa}')
print('Dirija sempre com sinto de segurança!')
