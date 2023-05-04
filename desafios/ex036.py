casa = float(input('Valor da Casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Em quantos anos quitará o imovel? '))
excessao = salario * 30 / 100
mensal = anos * 12
prestacao = casa / mensal
if excessao < prestacao:
    print(f'Emprestimo Negado! Condição de pagamento e maior que : {excessao}.')
else:
    print(f'Emprestimo Aprovado! Condição de pagamento e menor que {excessao}')
print(f'Valor da prestação {mensal} x {prestacao:.2f} Total: {casa}')
