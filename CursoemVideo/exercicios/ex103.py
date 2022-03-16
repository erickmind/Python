def ficha(nome='<Desconhecido>', gols='0'):
    print(f'{" FICHA DO JOGADOR ":=^50}')
    print(f'Nome: {nome}')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'Gols feitos: {gols}')


jogador = str(input('Nome do jogador: '))
numGols = str(input('Número de gols: '))

if jogador == '' and numGols == '':
    ficha()
elif jogador == '' and numGols != '':
    ficha(gols=numGols)
elif jogador != '' and numGols == '':
    ficha(nome=jogador)
else:
    ficha(jogador, numGols)

