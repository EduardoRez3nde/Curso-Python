from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!', end='')
        print()
        print('-='*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
