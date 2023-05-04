from datetime import date
print(f'====CONFEDERAÇÃO NACIONAL DE NATAÇÃO =====')
nascimento = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nascimento
if 0 <= idade <= 9:
    print(f'O atleta tem {idade} anos. Categoria MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. Categoria INFANTIL')
elif idade <= 18:
    print(f'O atleta tem {idade} anos. Categoria JUNIOR')
elif idade <= 20:
    print(f'O atleta tem {idade} anos. Categoria SÊNIOR')
else:
    print(f'O atleta tem {idade} anos. Categoria MASTER')
