valores = (int(input('Digite o Primeiro valor: ')),
           int(input('Digite o Primeiro valor: ')),
           int(input('Digite o Primeiro valor: ')),
           int(input('Digite o Primeiro valor: ')))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'a primeira que o 3 apareceu foi na posição {valores.index(3)}')
else:
    print('O valor 3 não foi encontrado!')
print(f'Os numeros pares digitados foram ', end='')
for v in valores:
    if v % 2 == 0:
        print(f'{v} ', end='')
