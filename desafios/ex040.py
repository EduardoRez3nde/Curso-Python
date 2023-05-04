nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua Média foi {media} REPROVADO!')
elif 5 <= media < 7:
    print(f'Sua média foi {media} RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media} PARABÉNS, APROVADO!!')