from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
while True:
    maior = 0
    print('=-'*20)
    menu = int(input('   [ 1 ] Somar\n   [ 2 ] Multiplicar\n   [ 3 ] Maior\n'
                     '   [ 4 ] Novos Números\n   [ 5 ] Sair\nQual a sua opção? '))
    print('=-'*20)
    if menu == 1:
        soma = n1 + n2
        print(f'A soma é: {n1} + {n2} = {soma}')
    elif menu == 2:
        multi = n1 * n2
        print(f'A multiplicação é: {n1} x {n2} = {multi}')
    elif menu == 3:
        if n1 > n2:
            print(f'O numero {n1} é maior que {n2}')
        else:
            print(f'O numero {n2} é maior que {n1}')
    elif menu == 4:
        print('Digite novamente os valores.')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(1)
        break
    sleep(2)
print('Volte Sempre!')
