tabela = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional',
          'Fluminense', 'Cruzeiro', 'Grêmio', 'São Paulo', 'Vasco',
          'Atlético-MG', 'Santos', 'Bragantino', 'Flamengo',
          'Athetico-PR', 'Bahia', 'Goiás', 'Corinthians', 'Cuiabá',
          'Coritiba', 'América-MG')
print(f'Lista dos clubes Do Brasileirão: {tabela}')
print('='*50)
print(f'Os 5 primeriros são: {tabela[:5]}')
print('='*50)
print(f'Os ultimos 4 são: {tabela[-4:]}')
print('='*50)
print(f'Clubes em ordem alfabetica: {sorted(tabela)}')
print('='*50)
print(f'O Flamengo esta na {tabela.index("Flamengo")+1}ª posição')
print('='*50)
