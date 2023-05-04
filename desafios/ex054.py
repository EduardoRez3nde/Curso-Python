frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um palíndromo!')
