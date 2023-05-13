from random import randint
from time import sleep
from operator import itemgetter # para ordenar o dicionario
valores = dict()
jogadores = list()
maior = 0
print('VALORES SORTEADOS:')
for v in range(1, 5):
    dado = randint(1, 6)
    valores[f'jogador{v}'] = dado
    print(' '*3, f'O jogador{v} tirou {dado} no dado.')
    sleep(1)
jogadores = sorted(valores.items(), key=itemgetter(1), reverse=True) # Para ordenar em ordem decrescente
print('RANKING DOS JOGADORES: ')
for k, c in enumerate(jogadores):
    print(f'  - {k+1}º lugar: {c[0]} com {c[1]}')
    sleep(1)
