sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Comando incorreto. Por favor, insira corretamente.')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
print('O sexo digitado foi: {}'.format(sexo))
