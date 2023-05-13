p = dict()
pessoas = list()
media = 0
while True:
    p.clear()
    p['nome'] = str(input('Nome: ').title())
    p['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while p['sexo'] not in 'MF':
        if p['sexo'] != 'MF':
            print('ERRO! Por Favor, digite somente M ou F.')
        p['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    p['idade'] = int(input('Idade: '))
    media += p['idade']
    pessoas.append(p.copy())
    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        if resp != 'SN':
            print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('='*40)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media/len(pessoas):5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media/len(pessoas):
        for k, v in p.items():
            print(f'    {k} = {v}; ', end='')
        print()
print('>>>> ENCERRADO >>>>')
