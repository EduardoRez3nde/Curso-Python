import math

angulo = float(input('Ângulo: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f'O valor do seno é: {seno:.2f}')
print(f'O valor do cosseno é: {cosseno:.2f}')
print(f'O valor da tangente é: {tangente:.2f}')
