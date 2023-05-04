num = soma = cont = 0
while num != 999:
    num = int(input('Digite um  numero [ 999 ] Sair: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Você Digitou {cont} a soma foi {soma}')
