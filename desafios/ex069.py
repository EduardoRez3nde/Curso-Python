from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU IMPAR? ')
print('=-'*30)
cont = 0
while True:
    valor = int(input('Diga um Valor? '))
    pc = randint(1, 10)
    total = valor + pc
    par_imp = ' '
    while par_imp not in 'PI':
        par_imp = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('=' * 40)
    print(f'Você jogou {valor} e o computador {pc}. Total {total} ', end='')
    if total % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU IMPAR')
    print('=' * 40)
    if par_imp == 'P':
        if total % 2 == 0:
            cont += 1
        elif total % 2 == 1:
            print('VOCÊ PERDEU!')
            break
    elif par_imp == 'I':
        if total % 2 == 1:
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Você VENCEU!\nVamos Jogar Novamente...')
print(f'GAME OVER! Você Venceu {cont} vezes.')
