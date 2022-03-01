nome = input('Digite um nome: ')
nome = nome.upper()
#if 'SILVA' in nome:
if nome.find('SILVA') != -1:
    print('A pessoa tem Silva no nome!')
else:
    print('A pessoa não tem Silva no nome!')
