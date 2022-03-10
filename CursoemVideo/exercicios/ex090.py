boletim = {}

boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['media'] = float(input('Digite a média do aluno: '))

if boletim['media'] < 5:
    boletim['situacao'] = 'Reprovado!'
elif 5 < boletim['media'] <= 7:
    boletim['situacao'] = 'Recuperação!'
else:
    boletim['situacao'] = 'Aprovado!'
print(f'''
Nome: {boletim['nome']}
Média: {boletim['media']}
Situação: {boletim['situacao']}''')

#for k, v in boletim.items():
#    print(f'{k} é {v}')
