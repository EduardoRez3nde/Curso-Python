s = cont = 0
for v in range(1, 501):
    if v % 1 == 0 and v % 3 == 0:
        if v % 2 == 1:
            s += v
            cont += 1
print(f'A soma de todos os {cont} numeros multiplos de três é: {s}')
