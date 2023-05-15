from random import randint
from time import sleep


def sorteio(lista):
    print(f'Sorteando {len(numeros)} valores da lista: ', end='')
    for n in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    print(f'Somando os valores pares de {lista} ', end='')
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'temos {soma}', end='')


numeros = list()
sorteio(numeros)
somapar(numeros)
