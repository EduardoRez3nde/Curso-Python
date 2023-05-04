num = int(input('Digite um numero: '))
menu = int(input('1 Binário\n2 Octal\n3 Hexadecimal ' ))
if menu == 1:
    binario = bin(num)
    print(f'O numero {num} em binário é {binario[2:]}')
elif menu == 2:
    octal = oct(num)
    print(f'O numero {num} em octal é {octal[2:]}')
elif menu == 3:
    hexa = hex(num)
    print(f'O numero {num} em hexadecimal é {hexa[2:]}')
