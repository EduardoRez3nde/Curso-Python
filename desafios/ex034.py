salario = float(input('Salário do funcionario: R$ '))
if salario > 1250:
    novo = (salario * 10 / 100) + salario
    print(f'Seu salário teve um aumento de 10% Total: {novo}')
else:
    novo = (salario * 15 / 100) + salario
    print(f'Seu salário teve uma aumento de 15% Tota: {novo}')
