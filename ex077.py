print('='*45)
print('           LISTAGEM DE PREÇOS')
print('='*45)
lista = ('HardDisk', 250, 'Memoria Ram', 190, 'SSD-480GB', 350,
         'Placa Video', 2200, 'Fonte', 310.99, 'Placa Mãe', 780,
         'Processador', 1400, 'mouse', 220.30, 'Monitor', 1300,
         'Teclado', 150, 'Gabinete', 330.50)
for v in range(len(lista)):
    if v % 2 == 0:
        print(f'{lista[v]:.<30}R$   ', end='')
    if v % 2 == 1:
        print(f'{lista[v]:.2f}')
print('='*45)
