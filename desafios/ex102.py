def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos:  NÃO VOTA.'


nascimento = int(input('Ano de Nascimento: '))
print(f'{voto(nascimento)}')
