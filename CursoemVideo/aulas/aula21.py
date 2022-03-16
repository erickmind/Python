#Interactive Help
help(print)
print('='*50)

print(input.__doc__)
print('='*50)


#DOCSTRING
def contador(i, f, p):
    """
    -> Faz uma contagem na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Erick Kussumoto do Nascimento
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)
print('='*50)


#Variáveis opcionais
def somar(a=0, b=0, c=0):
    """
    -> Soma três valores
    :param a: Primeiro valor a ser somado
    :param b: Segundo valor a ser somado
    :param c: Terceiro valor a ser somado
    :return: Sem retorno
    Feito por Erick Kussumoto
    """
    s = a + b + c
    print(f'A soma é {s}')


somar(1, 2)
somar(c=3, a=1)


#Escopo de variáveis


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


def funcao2():
    global n1
    n1 = 3
    print(f'N1 dentro vale {n1}')



n1 = 2
funcao()
print(f'N1 global vale {n1}')
funcao2()
print(f'N1 global vale {n1}')


#Retorno de funções
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f += c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1} {f2} {f3}')

