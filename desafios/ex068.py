from time import sleep
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*30)
    if num < 0:
        break
    for n in range(1, 11):
        multi = num * n
        print(f'{num} x {n} = {multi}')
    print('='*30)
print('Encerrando....')
sleep(2)
print('Volte Sempre!')
