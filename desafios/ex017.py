import math
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'O valor da Hipotenusa é: {hipotenusa:.2f}')
