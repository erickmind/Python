nome = str(input('Digite um nome: ')).strip()
nome = nome.split()
print('Primeiro: {}'.format(nome[0]))
print('Último: {}'.format(nome[len(nome)-1]))
