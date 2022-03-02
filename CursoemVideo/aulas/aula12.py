nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Erick':
    print('Seu nome é maneiro!')
elif nome in 'Ana Juliana Claudia Jéssica':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
