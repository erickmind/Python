jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for p in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = gols
jogador['total'] = sum(jogador['gols'])

print('='*50)
print(jogador)
print('='*50)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for p in range(0, jogador['partidas']):
    print(f'Na partida {p}, fez {jogador["gols"][p]} gols.')
print(f'Foram {jogador["total"]} gols.')
