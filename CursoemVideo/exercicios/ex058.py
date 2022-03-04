import random

print('{:=^40}'.format(' JOGO DE ADIVINHAÇÃO '))
print('Em qual número estou pensando?')
num = random.randint(0, 10)
escolha = int(input('Digite seu palpite de 0 a 10: '))
cont = 1
while escolha != num:
    cont += 1
    if escolha > num:
        escolha = int(input('\033[31mMenos... Tente novamente:\n\033[m'))
    else:
        escolha = int(input('\033[31mMais... Tente novamente:\n\033[m'))
print('Parabéns! O número em que pensei foi {}'.format(num))

if cont == 1:
    print('\033[35mVocê levou {} tentativa para acertar!\033[m'.format(cont))
elif cont <= 3:
    print('\033[33mVocê levou {} tentativas para acertar!\033[m'.format(cont))
elif cont <= 5:
    print('\033[32mVocê levou {} tentativas para acertar!\033[m'.format(cont))
else:
    print('\033[31mVocê levou {} tentativas para acertar!\033[m'.format(cont))
