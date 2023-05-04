import random
lista_alunos = []
for aluno in range(1, 5):
    alunos = str(input('Aluno: '))
    lista_alunos.append(alunos)
random.shuffle(lista_alunos)
print(lista_alunos)
