from exercicios.ex107.utilidadesCeV import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p, False)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {p}, temos {moeda.diminuir(p, 13, True)}')
