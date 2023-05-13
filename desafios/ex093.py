from datetime import date
atual = date.today().year
dados = dict()
while True:
    dados['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    dados['idade'] = atual - nasc
    dados['ctps'] = int(input('Carteira de Trabalho: (0 Não Possui) '))
    if dados['ctps'] == 0:
        break
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    apos = dados['contratação'] + 35 - nasc
    dados['aposentadoria'] = apos
    break
print('=-'*30)
for keys, value in dados.items():
    print(f'   - {keys} tem o valor {value}')
print('=-'*30)
