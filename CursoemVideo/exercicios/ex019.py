import random
alunos = []
for i in range(4):
    alunos.append(input('Digite o nome do aluno: '))
print('O aluno sorteado foi: {}'.format(alunos[random.randrange(0,4,1)]))
