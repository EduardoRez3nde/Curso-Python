valores = list()
while True:
    valor = int(input('digite um valor: '))
    resp = ' '
    if valor in valores:
        print('Valor duplicado! Não vou adicionar.')
    while valor not in valores:
        valores.append(valor)
        valores.sort()
        print('valor adicionado com sucesso!')
    while resp not in 'SN':
        resp = str(input('Quer Continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print('='*40)
print(f'Você digitou os valores {valores}')
