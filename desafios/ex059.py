from random import randint
total = 0
print('-='*20)
print('Computador pensei em um numero, consegue advinhar? ')
print('-='*20)
pc = randint(0, 10)
while True:
    player = int(input('Qual sua Jogada? '))
    total += 1
    if player > pc:
        print('Menos')
    else:
        print('mais')
    if player != pc:
        print('Você Errou! Tente Novamente!')
    else:
        print('Parabéns! Você Acertou!')
        break
print('-='*20)
print(f'Computador Jogou: {pc}\nJogador Jogou: {player}')
print(f'Você Precisou de {total} jogadas Para acertar.')
print('-='*20)
