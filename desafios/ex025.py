nome = str(input('Nome Completo: ').upper())
santo = nome.count('SILVA')
if santo == 1:
    print(f'Seu nome tem a palavra Silva')
else:
    print(f'Seu nome não tem a palavra Silva')
