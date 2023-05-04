cidade = str(input('Cidade: ').upper())
santo = cidade.split()
if santo[0] == 'SANTO':
    print(f'Sua cidade começa com a palavra Santo')
else:
    print(f'Não começa com a palavra Santo')
