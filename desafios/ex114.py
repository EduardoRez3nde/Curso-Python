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


def leia_float(num):
    while True:
        try:
            valor = float(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero real válido!\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[0;31mO usuario encerrou antes de digitar os dados.\033[m')
            return 0
        else:
            return valor


i = leia_int('digite um inteiro: ')
r = leia_float('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
