sexo = str(input('Sexo: [M/F]').strip().upper()[0])
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos! Insira Novamente: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
