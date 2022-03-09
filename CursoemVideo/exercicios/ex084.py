lista = []
pessoas = []
maior = 0
menor = 0

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    lista.append(nome)
    lista.append(peso)
    if len(pessoas) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    pessoas.append(lista[:])
    lista.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

print(f'O número de pessoas cadastradas é {len(pessoas)}')

print(f'As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nAs pessoas mais leves são: ', end='')

for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
