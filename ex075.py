from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10))
print('Os valores sorteados foram: ', end='')
for v in valores:
    print(v, end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor numeros sorteado doi {min(valores)}')
