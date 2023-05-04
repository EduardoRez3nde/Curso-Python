import random
alunos = []
for i in range(1, 5):
    alun = str(input('aluno: '))
    alunos.append(alun)
sorteio = random.choice(alunos)
print(f'O sorteado foi: {sorteio}')
