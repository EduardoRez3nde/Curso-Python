from time import sleep


def maior(*valores):
    print('-='*30)
    print('Analisando os valores passados...')
    cont = maior_valor = 0
    for v in valores:
        print(f'{v} ', end='')
        sleep(0.5)
    for valor in valores:
        if cont == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
        cont += 1
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {maior_valor}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
