cont = soma = maior = menor = 0
while True:
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if resp == 'N':
        break
media = soma / cont
print(f'Você digitou {cont} numeros e a  media foi {media:.2f}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
