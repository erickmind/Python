for i in range(0, 4):
    peso = float(input('Digite o peso da pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso é {}kg'.format(menor))
print('O maior peso é {}kg'.format(maior))
