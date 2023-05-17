def ajuda(func):
    escreva(f'Acessando o manual do comando \'{func}\'', c='azul')
    print(cor['roxo'], end='')
    help(func)
    print(cor['roxo'], end='')


def escreva(msg, c='semcores'):
    tamanho = len(msg) + 4
    print(cor[c], end='')
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cor['semcores'], end='')


cor = {'semcores': "\033[m", 'vermelho': "\033[0;30;41m",
       'verde': "\033[0;30;42m", 'amarelo': "\033[0;30;43m",
       'azul': "\033[0;30;44m", 'roxo': "\033[0;30;45m",
       'branco': "\033[7;30m"}

while True:
    escreva('SISTEMA DE AJUDA PyHelp', c='verde')
    funcao = str(input('Função ou Biblioteca >> '))
    if funcao.upper() == 'FIM':
        break
    else:
        ajuda(funcao)
escreva('ATÉ LOGO', c='vermelho')
