def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    for i, v in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{v}\033[m')
    print(linha())
    opcao = leia_int('\033[32mSua Opção: \033[m')
    return opcao


def leia_int(num):
    while True:
        try:
            valor = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero real válido!\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[0;31mO usuario encerrou antes de digitar os dados.\033[m')
            return 0
        else:
            return valor
