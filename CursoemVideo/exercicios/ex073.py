tabela = ('America-MG', 'Athletico-PR', 'Atlético Goianiense', 'Atlético Mineiro', 'Avaí',
          'Botafogo', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense',
          'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos',
          'São Paulo')

print('{:=^40}'.format('TABELA DO BRASILEIRÃO'))

for pos, time in enumerate(tabela):
    print(f'{pos+1}: {time}')

print('-'*50)

print(f'Os cinco primeiros colocados da tabela são: {tabela[:5]}')

print(f'Os quatro últimos colocados da tabela são: {tabela[-4:]}')

print(f'Os times em ordem alfabética são: {sorted(tabela)}')

santos = 'Santos'
print(f'O Santos está na {tabela.index(santos)+1} posição da tabela!')


