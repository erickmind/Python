val = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
val3 = int(input('Digite o terceiro valor: '))

menor = val
if val2 < val and val2 < val3:
    menor = val2
if val3 < val and val3 < val2:
    menor = val3
maior = val
if val2 > val and val2 > val3:
        maior = val2
if val3 > val and val3 > val:
        maior = val3

print('O maior número é {} e o menor é {}'.format(maior, menor))
