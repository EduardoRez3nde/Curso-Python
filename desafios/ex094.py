dados = dict()
gols = list()
dados['nome'] = str(input('Nome do Jogador: ').title())
partida = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(0, partida):
    gols.append(int(input(f'   - Quantos gols na partida {p+1}? ')))
dados['gols'] = gols.copy()
dados['total'] = sum(gols)
print('='*50)
print(dados)
print('='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('='*40)
print(f'O jogador {dados["nome"]} jogou {partida} partidas.')
for i, v in enumerate(gols):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')
