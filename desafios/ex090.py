from time import sleep
alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print('-'*25)
print('No.', ' '*2, 'NOME', ' '*5, 'MÉDIA')
print('-'*25)
for i, v in enumerate(alunos):
    print(f'{i:<6} {v[0]:<12} {v[2]}')
print('-'*25)
while True:
    individual = int(input('Mostrar a nota de qual aluno? sair[999] '))
    if individual == 999:
        print('Finalizando...')
        sleep(1)
        break
    if individual <= len(alunos):
        print(f'Notas de {alunos[individual][0].title()} são {alunos[individual][1]}')
        print()
print('Volte Sempre!')
