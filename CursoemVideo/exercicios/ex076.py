prod = ('Lápis', 2,
        'Borracha', 3,
        'Lapiseira', 6,
        'Caneta', 5,
        'Estojo', 10)

print(f'{"TABELA DE PREÇOS":-^50}'.format())

for i in range(0, len(prod), 2):
    print(f'{prod[i]:.<40} R$ {prod[i+1]:>5.2f}')

print('-'*50)