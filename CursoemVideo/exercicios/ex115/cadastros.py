from exercicios.ex115.lib.interface import *


def cadastra(nome='Desconhecido', idade=0):
    f = open('arquivoRegistro.txt', "a+")
    try:
        f.write(f'{nome:<30} {idade:>3} anos')
        f.write('\n')
    except:
        print(f'\033[31mErro ao ler o arquivo\033[m')
    f.close()


def lista():
    cabecalho(' PESSOAS CADASTRADAS ')
    try:
        f = open('arquivoRegistro.txt', "r")
    except FileNotFoundError:
        print(f'\033[31mNão existem pessoas cadastradas no sistema!\033[m')
        return
    if f.mode == 'r':
        content = f.read()
        print(content)
