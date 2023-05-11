pessoas = list()
pessoa = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for i, v in enumerate(pessoas):
    if v[1] == maior:
        print(f'[{v[0]}] ', end='')
print(f'\nO menor peso foi de {menor} ', end='')
for i, v in enumerate(pessoas):
    if v[1] == menor:
        print(f'[{v[0]}] ', end='')
