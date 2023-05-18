def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, taxa=0):
    porcent = n + (n * taxa / 100)
    return porcent


def diminuir(n=0, taxa=0):
    res = n - (n * taxa / 100)
    return res


def moeda(n=0, simbol='R$'):
    return f'{simbol}{n:,.2f}'.replace('.', ',')
