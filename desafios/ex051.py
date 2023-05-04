s = cont = 0
for v in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você informou {cont} numeros pares e a soma é: {s}')
