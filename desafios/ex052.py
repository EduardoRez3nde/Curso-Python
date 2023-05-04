termo = int(input('Primerio Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end=' -> ')
