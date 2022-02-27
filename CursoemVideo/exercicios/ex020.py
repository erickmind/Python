import random
alunos = []
for i in range(4):
    alunos.append(input('Digite o nome do aluno: '))
random.shuffle(alunos)
print('A ordem de apresentação será:\n{}'.format(alunos))

