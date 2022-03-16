def notas(* notas, situacao=False):
    """
    Gera um boletim usando várias notas de alunos. Mostra qual é a maior e menor nota
    e mostra a média da turma. Mostra a situação da turma caso seja desejado.
    :param notas: Lista de notas passadas como parâmetro da função
    :param situacao: (Opcional) True: Retorna a situação da turma em relação à média
                                False: Não retorna a situação da turma
    :return: Retorna um dicionário de alunos com as notas, a quantidade de notas,
            a maior e menor nota e a situação
    """
    alunos = {}
    alunos['notas'] = notas
    alunos['quant'] = len(notas)
    alunos['media'] = sum(notas)/len(notas)
    alunos['maior'] = max(notas)
    alunos['menor'] = min(notas)
    if situacao:
        if alunos['media'] < 5:
            alunos['situação'] = 'RUIM'
        elif 5 <= alunos['media'] < 7:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'BOA'
    return alunos


boletim = dict()
boletim = notas(5.5, 2.5, 1.5, situacao=True)
print(boletim)
boletim = notas(3, 5, 6, situacao=True)
print(boletim)
boletim = notas(5, 5, 5, situacao=False)
print(boletim)
boletim = notas(10, 0, 5)
print(boletim)
boletim = notas(10, 7, 9, situacao=True)
print(boletim)
help(notas)

