valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
pares = col3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end='')
        if valores[l][c] % 2 == 0:
            pares += valores[l][c]
    print()
print('='*30)
print(f'A soma dos valores pares é {pares}')
for l in range(0, 3):
    col3 += valores[l][2]
print(f'A soma dos valores da terceira coluna é {col3}')
for c in range(0, 3):
    if c == 0:
        maior = valores[1][c]
    elif valores[1][c] > maior:
        maior = valores[1][c]
print(f'O maior valor da segunda linha é {maior}')
