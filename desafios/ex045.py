from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jogador = int(input('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA'))
if jogador == pc:
    print(f'O coputador escolheu: {itens[pc]}')
