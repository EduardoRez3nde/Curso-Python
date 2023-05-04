n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')
