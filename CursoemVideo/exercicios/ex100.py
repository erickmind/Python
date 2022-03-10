from random import randint


def sorteia(list):
    print('Sorteando 5 valores para a lista:')
    for i in range(0, 5):
        list.append(randint(1, 100))
    print(list)
    print('-'*50)


def somaPar(list):
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares é {soma}')


lista = []
sorteia(lista)
somaPar(lista)
