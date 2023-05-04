soma = c = 0
while True:
    n = int(input('Digite um valor [ 999 ] Parar: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'A soma dos {c} valores foi {soma}')
