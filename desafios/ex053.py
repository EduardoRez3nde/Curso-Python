num = int(input('Digite um numero: '))
primo = True
for n in range(2, num):
    if num % n == 0:
        primo = False
        break
if primo:
    print(f'O numero {num} é primo.')
else:
    print(f'O numero {num} não é primo.')
