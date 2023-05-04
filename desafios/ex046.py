from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
player = int(input('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n'))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
print('=-'*20)
print(f'Você escolheu {itens[player]}')
sleep(0.2)
print(f'Computador escolheu {itens[pc]}')
print('=-'*20)
if pc == 0:
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('Parabéns! Você Venceu!')
    elif player == 2:
        print('Que pena! Você perdeu!')
elif pc == 1:
    if player == 0:
        print('Quem Pena! Você Perdeu!')
    elif player == 1:
        print('Empate')
    elif player == 2:
        print('Parabéns! Você Venceu!')
elif pc == 2:
    if player == 0:
        print('Parabéns! Você Venceu!')
    elif player == 1:
        print('Que Pena! Você Perdeu!')
    elif player == 2:
        print('Empate!')
print('=-'*20)