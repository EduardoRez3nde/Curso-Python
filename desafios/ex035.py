r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print(f'Os segmentos acima PODEM FORMAR TRIÂNGULO.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO.')
