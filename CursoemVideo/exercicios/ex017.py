from math import hypot
catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é: {:.2f}'.format(hypot(catOp, catAd)))

