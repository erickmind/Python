palavras = ('palavra', 'amigo', 'pessoa', 'casa', 'apartamento', 'python')

for pal in palavras:
    print(f'As vogais de "{pal}" são: ', end='')
    for letra in pal:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print('')
