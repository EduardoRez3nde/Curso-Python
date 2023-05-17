def notas(*dados, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param dados: um ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    valores = {'total': len(dados), 'maior': max(dados),
               'menor': min(dados), 'media': sum(dados) / len(dados)}
    if situacao:
        if valores['media'] < 5:
            valores['situacao'] = 'RUIN'
        elif 5 <= valores['media'] <= 6:
            valores['situacao'] = 'RAZOAVEL'
        elif 6 < valores['media'] <= 7.5:
            valores['situacao'] = 'BOA'
        else:
            valores['situacao'] = 'ÓTIMO'
    return valores


resp = notas(5.5, 2.5, 1.5, situacao=True)
print(resp)
help(notas)
