def fatorial(num, show=False):
    """
    Calculadora de fatorial
    :param num: Valor a ser calculado o fatorial
    :param show: (opcional) Mostrar ou não a conta
    :return: Sem retorno
    """
    total = 1
    for i in range(num, 0, -1):
            total *= i
            if show == True:
                print(i, end='')
                if i == 1:
                    print(' = ', end='')
                else:
                    print(' x ', end='')
    print(total)


print(f'{" CALCULADORA DE FATORIAL ":=^50}')
fatorial(int(input('Digite o valor a ser calculado: ')))
fatorial(int(input('Digite o valor a ser calculado: ')), True)
help(fatorial)
