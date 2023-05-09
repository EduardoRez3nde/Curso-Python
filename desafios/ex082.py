valores = list()
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    cont += 1
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)
print('=-'*30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
print(f'O valor 5 ', end='')
if 5 in valores:
    print('faz parte da lista!', end='')
else:
    print('Não foi encontrado na lista!', end='')
