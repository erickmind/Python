def soma(a, b):
    s = a + b
    print(f'O valor de A é {a} e o valor de B é {b}')
    print(f'A soma de {a}+{b} é {s}')

def conta(* val):
    print(f'Tamanho de conta é: {len(val)}')
    for i in val:
        print(i)

def vetTest(lista):
    print(f'Tamanho de vetTest é: {len(lista)}')
    for i in lista:
        print(i)

soma(2, 1)
soma(b=3, a=4)
conta(2)
conta(1, 2, 3, 4, 5)
vet = [1, 2, 3, 4, 5, 6]
vetTest(vet)

