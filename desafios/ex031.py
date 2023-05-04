distancia = int(input('Distância da Viagem [km]: '))
preco = 0
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem é: {preco}')
