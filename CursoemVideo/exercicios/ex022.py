nome = str(input('Digite seu nome: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
print('O nome em maiúsculo é: {}'.format(maiusculo))
print('O nome em minúsculo é: {}'.format(minusculo))
print('O número de letras na frase é: {}'.format(len(nome) - nome.count(' ')))
nomeAux = nome.split()
print('O número de letras no primeiro nome é: {}'.format(len(nomeAux[0])))


