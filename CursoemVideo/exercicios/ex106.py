c = ('\033[m',
     '\033[0;97;41m',
     '\033[0;97;42m',
     '\033[0;97;43m',
     '\033[0;97;44m',
     '\033[0;97;45m',
     '\033[7;97m'
     )


def helpMe(command):
    from time import sleep
    titulo(f'Acessando o manual do comando \'{command}\'', 4)
    sleep(1)
    print(c[6], end='')
    help(command)
    print(c[0], end='')


def titulo(msg, cor=0):
    from time import sleep
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


com = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    com = str(input('Função ou Biblioteca: '))
    if com.upper() in 'FIM':
        titulo('FIM DO PROGRAMA', 1)
        break
    helpMe(com)
