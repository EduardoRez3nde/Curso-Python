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
