'''num = int(input('Digite um Numero Para Saber o fatorial: '))
fatorial = 1
for n in range(num, 0, -1):
    fatorial *= n
    print(f'{n} x ', end='')
print(fatorial, end='')
'''

num = int(input('Digite um numero: '))
fatorial = 1
print(f'Calculando {num}! = ', end='')
while num > 0:
    fatorial *= num
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    num -= 1
print(fatorial)
