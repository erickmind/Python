pessoa = {}
lista = []
idades = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Digite o sexo: [M/F] ')).strip().upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    idades += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja inserir mais pessoas? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

print('='*50)
print(f'O número de pessoas cadastradas foi {len(lista):.0f}.')
print(f'A idade média do grupo é {int(idades/len(lista))} anos.')
print(f'Mulheres do grupo:', end=' ')
for p in lista:
    if p['sexo'][0].upper() in 'F':
        print(p['nome'], end=' ')
print(f'\nLista de pessoas acima de {int(idades/len(lista))} anos:', end=' ')
for p in lista:
    if p['idade'] > idades/len(lista):
        print(p['nome'], end=' ')
