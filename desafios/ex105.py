def leia_int(num):
    validador = False
    valor = 0
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            valor = int(numero)
            validador = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido!\033[m')
        if validador:
            break
    return valor


n = leia_int('digite um numero:')
print(f'Você acabou de digitar o numero {n}')
