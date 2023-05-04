from random import randint
from time import sleep  #delay
pc = randint(0, 5)
print(f'Computador: Pensei em um numero, consegue advinhar?')
sleep(0.5)
player = int(input('Digite um numero entre 0 e 5: '))
print('-=-'*10)
print('Processando...')
sleep(2)
print(f'Jogador jogou: {player}')
sleep(0.8)
print(f'O computador jogou: {pc}')
sleep(0.8)
print('-=-'*10)
if player == pc:
    print('Parabéns! Você Acertou!')
else:
    print('Você Errou! Tente Novamente!')
