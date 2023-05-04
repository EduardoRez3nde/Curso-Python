from datetime import date
atual = date.today().year
maior = menor = 0
for p in range(1, 8):
    nascimento = int(input(f'Ano de Nascimento da {p}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Total de pessoas MAIORES de idade: {maior} pessoas')
print(f'Total de pessoas MENORES de idade: {menor} pessoas')
