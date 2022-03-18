def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('SISTEMA DE ARQUIVO v1.0')
    for c, item in enumerate(lista):
        print(f'\033[33m{c+1}\033[m - \033[36m{item}\033[m')
    print(linha())


