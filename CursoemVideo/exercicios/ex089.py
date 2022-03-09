aluno = []
boletim = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2)/2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja inserir mais um aluno? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

print('='*50)
print(f'{"Boletim da turma:":^50}')
print('='*50)
(print(f'{"No.":<4}{"ALUNO":<10}{"MÉDIA":>8}'))
print('-' * 50)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[3]:>8}')
    print('-' * 50)

while True:
    opcao = -2
    while opcao < -1 or opcao > len(boletim)-1:
        opcao = int(input('Qual aluno deseja ver a nota individual? (-1 para sair) '))
    if opcao == -1:
        break
    (print(f'{"ALUNO":<4}{"NOTA 1":>10}{"NOTA 2":>8}'))
    print(f'{boletim[opcao][0]:<4}{boletim[opcao][1]:>10}{boletim[opcao][2]:>8}')

print('FIM DO PROGRAMA')
