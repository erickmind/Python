import random
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
val = int(input('Em que número pensei? '))
ran = random.randrange(0, 5, 1)
if ran == val:
    print('Parabéns! Você acertou o valor!')
else:
    print('O valor correto era {}'.format(ran))
