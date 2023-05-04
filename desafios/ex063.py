print('=-'*15)
print('       GERADOR DE PA')
print('=-'*15)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{primeiro} -> ', end='')
        primeiro += razao
        c += 1
    mais = int(input('\nQuantos Termos a Mais? '))
print('Finalizando...')
print(f'Total de Termos mostrados: {total} Termos ')
