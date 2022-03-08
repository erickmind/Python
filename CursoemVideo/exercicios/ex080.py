lista = []

for i in range(0, 5):
    val = int(input('Digite um valor: '))
    index = 0
    if len(lista) == 0 or val > lista[-1]:
        lista.append(val)
        print('Adicionando ao final da lista...')
    else:
        while index < len(lista):
            if val <= lista[index]:
                lista.insert(index, val)
                print(f'Adicionando na posição {index} da fila')
                break
            index += 1
print(lista)
