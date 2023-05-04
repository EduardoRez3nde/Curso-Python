maior = masc = fem = 0
while True:
    print('=' * 40)
    print('          CADASTRO DE PESSOAS')
    print('=' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    print('=' * 40)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print('======= FIM DO PROGRAMA ========')
print(f'Total de Pessoas mais de 18 anos: {maior}')
print(f'Ao todo temos {masc} homens cadastrados.')
print(f'E temos {fem} mulheres com menos de 20 anos.')
