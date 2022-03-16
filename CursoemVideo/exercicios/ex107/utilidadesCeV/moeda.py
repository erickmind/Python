def aumentar(val, aum, opcao=False):
    '''
    Aumenta o valor por uma porcentagem
    :param val: Valor
    :param aum: Valor de aumento (em %)
    :param opcao: Flag para indicar se retorna a mensagem formatada em valor monetário
    :return: Se opcao = False: Retorna o valor sem formatação
                      = True: Retorna a string do valor formatado
    '''
    val = val + val * aum/100
    return val if opcao is False else moeda(val)

def diminuir(val, dim, opcao=False):
    '''
    Aumenta o valor por uma porcentagem
    :param val: Valor
    :param dim: Valor de diminuição (em %)
    :param opcao: Flag para indicar se retorna a mensagem formatada em valor monetário
    :return: Se opcao = False: Retorna o valor sem formatação
                      = True: Retorna a string do valor formatado
    '''
    val = val - val * dim/100
    return val if opcao is False else moeda(val)


def dobro(val, opcao=False):
    '''
    Retorna o dobro do valor passado
    :param val: Valor
    :param opcao: Flag para indicar se retorna a mensagem formatada em valor monetário
    :return: Se opcao = False: Retorna o valor sem formatação
                      = True: Retorna a string do valor formatado
    '''
    val *= 2
    return val if opcao is False else moeda(val)


def metade(val, opcao=False):
    '''
    Retorna a metade do valor passado
    :param val: Valor
    :param opcao: Flag para indicar se retorna a mensagem formatada em valor monetário
    :return: Se opcao = False: Retorna o valor sem formatação
                      = True: Retorna a string do valor formatado
    '''
    val /= 2
    return val if opcao is False else moeda(val)


def moeda(val, moeda='R$'):
    '''
    Modifica o valor para que tenha formato monetário
    :param val: Valor
    :param moeda: String da formatação desejada
    :return: Retorna a string do valor formatado
    '''
    return f'{moeda}{val:.2f}'.replace('.', ',')


def resumo(p=0, aumento=10, diminuicao=5):
    '''
    Exibe vários cálculos aplicados em um valor passado
    :param p: Valor
    :param aumento: Valor de aumento (em %)
    :param diminuicao: Valor de diminuição (em %)
    :return: Sem retorno
    '''
    print('-'*40)
    print(f'{" RESUMO DO VALOR ":^40}')
    print('-' * 40)
    print(f'A metade de {p} é \t\t{metade(p, True)}')
    print(f'O dobro de {p} é \t\t\t{dobro(p, True)}')
    print(f'Aumentando {aumento}% de {p}: \t{aumentar(p, aumento, True)}')
    print(f'Diminuindo {diminuicao}% de {p}: \t{diminuir(p, diminuicao, True)}')
    print('-' * 40)
