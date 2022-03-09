from random import randint
from time import sleep

print(f'{" JOGUE NA MEGA SENA ":=^40}')

jogo = []
cartela = []

num = int(input('Digite o número de jogos a serem gerados: '))
for i in range(0, num):
    for j in range(0, 6):
        val = randint(1, 60)
        while val in jogo:
            val = randint(1, 60)
        jogo.append(val)
    jogo.sort()
    cartela.append(jogo[:])
    sleep(1)
    print(f'Jogo {i+1}: {jogo}')
    jogo.clear()

print(f'{" BOA SORTE! ":=^40}')

