print('=-'*15)
print('       GERADOR DE PA')
print('=-'*15)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    print(f'{primeiro} -> ', end='')
    primeiro += razao
    c += 1
print('Acabou.')
