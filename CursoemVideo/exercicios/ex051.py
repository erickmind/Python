print('10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
v = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    v += r
    print(v, end = ' ')
#for i in range(v, v + (10 - 1)*r + r, r):
#    print(i, end = ' ')