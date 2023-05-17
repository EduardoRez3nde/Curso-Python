def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(nome=n, gols=g))
