from exercicios.ex115.cadastros import cadastra, lista
from ex115.lib.interface import menu
from ex115.lib.utils import *

while True:
    escolha = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
    menu(escolha)
    opcao = leiaInt('Digite a opção desejada: ')
    if opcao == 1:
        lista()
    elif opcao == 2:
        cadastra(str(input('Digite o nome: ')), int(input('Digite a idade: ')))
    elif opcao == 3:
        print('-'*50)
        print('FIM DO PROGRAMA')
        break
    else:
        print('\033[31mPor favor, digite uma opção válida\033[m')

