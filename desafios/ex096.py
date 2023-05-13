dados = dict()
gols = list()
jogadores = list()
while True:
    dados.clear()
    gols.clear()
    dados['nome'] = str(input('Nome do Jogador: ').title())
    partida = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for p in range(0, partida):
        gols.append(int(input(f'   - Quantos gols na partida {p+1}? ')))
    dados['gols'] = gols.copy()
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Por Favor, digite apenas S ou N.')
    if resp in 'N':
        break
print('='*50)
print(f'{"COD":<6}{"NOME":<15}{"GOLS":<16}{"TOTAL"}')
print('='*50)
for i, v in enumerate(jogadores):
    print(f'{i:<6}{v["nome"]:<15}{str(v["gols"]):<17}{v["total"]}')
print('='*50)
while True:
    print('='*30)
    opc = int(input('Mostrar dados de qual jogador? [999] Sair'))
    if opc == 999:
        break
    if opc > len(jogadores):
        print(f'ERRO! Não exite jogador com o codigo {opc} informado! Tente Novamente.')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}')
        for i, v in enumerate(jogadores[opc]["gols"]):
            print(f'   => Na partida {i+1}, fez {v} gols.')
        print(f'Foi um total de {jogadores[opc]["total"]} gols')
