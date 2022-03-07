import time
import random
print('{:=^40}'.format(' Jogo do Par ou Ímpar '))

count = 0
while True:
    comp = random.randint(0, 10)
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('''Digite sua escolha:
            [P] Par
            [I] Ímpar\n''')).strip().upper()[0]
    val = int(input('Digite um valor: '))
    print('Par')
    time.sleep(1)
    print('ou')
    time.sleep(1)
    print('Ímpar!')
    print('-' * 40)
    print(f'Você jogou {val} e o computador {comp}')
    if opcao in 'P':
        if (comp+val) % 2 == 0:
            print(f'{comp+val} é par')
            print('\033[32mVocê ganhou!\033[m')
            print('Vamos jogar novamente...')
            print('-' * 40)
            count += 1
        else:
            print(f'{comp+val} é ímpar')
            print('\033[33mVocê perdeu! Adeus!\033[m')
            print('-' * 40)
            break
    elif opcao in 'I':
        if (comp+val) % 2 == 0:
            print(f'{comp+val} é par')
            print('\033[33mVocê perdeu! Adeus!\033[m')
            print('-' * 40)
            break
        else:
            print(f'{comp+val} é ímpar')
            print('\033[32mVocê ganhou!\033[m')
            print('Vamos jogar novamente...')
            print('-' * 40)
            count += 1
    time.sleep(1.5)
print(f'Você ganhou {count} vezes.')
print('FIM DO PROGRAMA')
