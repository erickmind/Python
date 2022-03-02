import random
import time
print('\033[1;35m-=-\033[m'*30)
print('\033[1;97;45m{: ^90}\033[m'.format('JOKENPÔ'))
print('\033[1;35m-=-\033[m'*30)
print('Escolha uma jogada:')
print('\033[35m1:\033[m Pedra\n\033[35m2:\033[m Papel\n\033[35m3:\033[m Tesoura')
jogada = int(input())
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!')

possib = {1: 'Pedra', 2:'Papel', 3:'Tesoura'}
jogadaComp = random.randint(1, 3)
print('Você jogou {}'.format(possib[jogada]))
print('O computador jogou: {}'.format(possib[jogadaComp]))
if (jogadaComp == 1 and jogada == 2) or (jogadaComp == 2 and jogada == 3) or (jogadaComp == 3 and jogada == 1):
    print('\033[32mGANHOU!\033[m')
elif jogadaComp == jogada:
    print('\033[33mEMPATOU!\033[m')
else:
    print('\033[31mPERDEU!\033[m')

