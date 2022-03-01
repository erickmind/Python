val = int(input('Digite um valor de 0 a 9999: '))
# if len(val) == 1:
#     print('unidade: {}'.format(val))
# elif len(val) == 2:
#     print('unidade: {}\ndezena: {}'.format(val[1], val[0]))
# elif len(val) == 3:
#     print('unidade: {}\ndezena: {}\ncentena: {}'.format(val[2], val[1], val[0]))
# elif len(val) == 4:
#     print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(val[3], val[2], val[1], val[0]))
# else:
#     print('Valor inválido!')
u = val // 1 % 10
d = val // 10 % 10
c = val // 100 % 10
m = val // 1000 % 10

print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(u, d, c, m))


