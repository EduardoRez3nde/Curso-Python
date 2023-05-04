peso = float(input('Peso: kg '))
altura = float(input('Altura: M '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}kg/m2. Você esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f}kg/m2. Você esta no peso ideal!')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f}kg/m2. Você esta em Sobrepeso!')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.2f}Kg/m2. Você esta em Obesidade!')
else:
    print(f'Seu IMC é {imc:.2f}kg/m2. Você esta em Obesidade Mórbida!')
