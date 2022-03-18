def leiaInt(txt):
    while True:
        try:
            val = int(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar esse número.\033[m')
            break
        except ValueError or KeyError:
            print(f'\033[31mPor favor, digite uma opção válida\033[m')
        else:
            return val
