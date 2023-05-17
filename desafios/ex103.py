def fatorial(num, show=False):
    """
    CALCULA FATORIAL DE UM NUMERO.
    :param num: O numero a ser calculado.
    :param show: (opcional) mostra ou não o calculo
    :return: o resultado
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(f'{fatorial(5, show=True)}')
help(fatorial)
