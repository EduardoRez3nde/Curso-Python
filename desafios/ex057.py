soma = 0
homem = ' '
maior = menor = 0
for p in range(1, 5):
    print(f'===== {p}ª PESSOA =====')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    soma += idade
    if sexo == 'M':
        if idade == 1:
            maior = idade
        elif idade > maior:
            maior = idade
            homem = nome
    if sexo == 'F':
        if idade < 20:
            menor += 1
media = soma / 4
print(f'A média de idade do grupo é: {media} anos')
print(f'O homem mais velho é: {homem}')
print(f'Ao todo são {menor} com mais de 20 anos')
