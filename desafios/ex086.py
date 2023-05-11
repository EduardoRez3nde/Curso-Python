valores = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}ª valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
        valores[0].sort()
    else:
        valores[1].append(valor)
        valores[1].sort()
print(f'O valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
