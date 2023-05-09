completa = list()
pares = list()
impar = list()
while True:
    valor = int(input('Digite um valor: '))
    completa.append(valor)
    resp = ' '
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('=-'*30)
print(f'A lista completa de valores é {completa}')
print(f'A lista de valores pares é {pares}')
print(f'A lista de valores impares é {impar}')
