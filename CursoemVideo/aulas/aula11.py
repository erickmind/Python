print('\033[4;97;45mOlá Mundo\033[m')

a = 3
b = 5
print('O valores são \033[32m{}\033[m e \033[35m{}\033[m'.format(a, b))

nome = 'Erick'
print('Muito prazer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m', 'azul': '\033[1;34m', 'amarelo': '\033[33m'}
print('Prazer novamente {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
