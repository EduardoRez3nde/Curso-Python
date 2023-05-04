print('='*30)
print('    SEQUÊNCIA DE FIBONACCI')
print('='*30)
termo = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ',end='')
cont = 0
while cont <= termo:
    t3 = t1 + t2
    print(f' -> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
