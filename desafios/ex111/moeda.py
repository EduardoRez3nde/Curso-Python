def moeda(n=float(0), simbol='R$'):
    return f'{simbol}{n:,.2f}'.replace('.', ',')


def metade(n=0, show=False):
    res = n / 2
    return res if not show else moeda(res)


def dobro(n=0, show=False):
    res = n * 2
    return res if not show else moeda(res)


def aumentar(n=0, taxa=0, show=False):
    res = n + (n * taxa / 100)
    return res if not show else moeda(res)


def diminuir(n=0, taxa=0, show=False):
    res = n - (n * taxa / 100)
    return res if not show else moeda(res)


def resumo(n=0, taxa=0, taxa2=0):
    print('-'*30)
    print('     RESUMO DO VALOR')
    print('-'*30)
    print(f'{"PREÇO ANALISADO:":<20}{moeda(n)}')
    print(f'{"DOBRO DO PREÇO:":<20}{moeda(dobro(n))}')
    print(f'{"METADE DO PREÇO:":<20}{moeda(metade(n))}')
    print(f'{taxa}{"%DE AUMENTO:":<17} {moeda(aumentar(n, taxa))}')
    print(f'{taxa2}{"%DE REDUÇÃO:":<18}{moeda(diminuir(n, taxa2))}')
    print('-'*30)
