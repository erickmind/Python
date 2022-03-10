from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            if i <= fim:
                print(i, end=' ')
            sleep(1)
    else:
        for i in range(inicio, fim-passo, -passo):
            if i >= fim:
                print(i, end=' ')
            sleep(1)
    print()
    print('='*50)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
pas = int(input('Passo: '))
contador(a, b, pas)
