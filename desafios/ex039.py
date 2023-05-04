from datetime import date
nascimento = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade < 18:
    print(f'Você tem {idade} anos. Faltam {18-idade} anos para se alistar.')
    print(f'ano de alistamento: {nascimento+18}')
elif idade == 18:
    print(f'Procure uma junta militar para se  alistar!')
else:
    print(f'Você tem {idade} anos. Passou {idade-18} anos.Procure uma junta do serviço militar!')
    print(f'Você deveria ter se alistado em {nascimento+18}')
