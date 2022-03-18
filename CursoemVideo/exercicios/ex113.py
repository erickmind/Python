def leiaInt(txt):
    success = False
    while not success:
        try:
            txt = int(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar esse número.\033[m')
            break
        except ValueError or KeyError:
            print(f'\033[31mErro! O valor digitado não é um número inteiro!\033[m')
        else:
            print(f'\033[33mO valor numérico digitado foi: {txt}\033[m')
            success = True


def leiaFloat():
    sucesso = False
    while not sucesso:
        try:
            txt = float(input('Digite um valor real: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro! O valor digitado não é um número real!\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuário\033[m')
            break
        else:
            print(f'O número real digitado foi: {txt}')
            sucesso = True


leiaInt()
leiaFloat()
