def leiaInt():
    txt = ' '
    while not txt.isnumeric():
        txt = str(input('Digite um valor numérico: '))
    print(f'O valor numérico digitado foi: {txt}')


leiaInt()
