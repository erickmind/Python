from random import randint
from time import sleep
from operator import itemgetter

print(f'{" Valores sorteados ":=^40}')
jogadores = {}
ranking = {}
for i in range(1, 5):
    nome = 'jogador'+f'{i}'
    val = randint(1, 6)
    jogadores[nome] = val
    print(f'{nome} tirou: {jogadores[nome]}')
    sleep(1)

ranking = sorted(jogadores.items(), reverse=True, key=itemgetter(1)) # Para pegar e ordenar pelo valor ([0]chave:[1]valor)
print(f'{" Ranking dos jogadores ":=^40}')
for k, v in enumerate(ranking):
    print(f'{k+1} Lugar : {v[0]} com {v[1]}.')
    sleep(1)
