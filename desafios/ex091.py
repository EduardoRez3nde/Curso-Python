aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if 7 > aluno['Media'] >= 5:
    aluno['Situação'] = 'Recuperação'
elif aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Parabéns! Aprovado.'
print('='*30)
for keys, value in aluno.items():
    print(f'  - {keys} é igual a {value}')
