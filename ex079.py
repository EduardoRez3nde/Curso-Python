'''valores = list()
for valor in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {valor}:')))
maior = max(valores)
menor = min(valores)
print('='*50)
print(f'Você digitou os valores {valores} ')
print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for i in range(len(valores)):
    if valores[i] == maior:
        print(f'{i}...', end='')
print(f'\nO Menor valor digitado foi {menor} nas posições ', end='')
for i in range(len(valores)):
    if valores[i] == menor:
        print(f'{i}... ', end='')'''

valores = list()
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}ª valor: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('='*40)
print(f'Você digitou os valores {valores} ')
print(f'O MAIOR valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO MENOR numero digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
