pessoas = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 55
print(pessoas)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(v, end=' ')
    print()

