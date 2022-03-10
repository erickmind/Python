jogador = {}
lista = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    count = 0
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(jogador['gols'])
    lista.append(jogador.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja inserir mais jogadores? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

print('='*50)
print(f'{"Cod":<3}{"Nome":>5}{"Gols":>10}{"Total":>15}')
for index, jog in enumerate(lista):
    print(f'{index:<3} {jog["nome"]:>5}      {jog["gols"]}{jog["total"]:>5}')
print('='*50)

while True:
    opcao = -2
    while opcao < -1 or opcao > len(lista)-1:
        opcao = int(input('Mostrar dados de qual jogador?[-1 para sair] '))
    if opcao == -1:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[opcao]["nome"]}:')
        for gol in range(0, lista[opcao]['partidas']):
            print(f'No jogo {gol+1} fez {lista[opcao]["gols"][gol]} gols.')
print('FIM DO PROGRAMA')


