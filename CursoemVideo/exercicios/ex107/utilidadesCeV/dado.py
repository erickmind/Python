def leiaDinheiro(txt):
    while True:
        ent = str(input(txt)).replace(',', '.')
        if ent.isalpha() or ent.strip() == '':
            print(f'\033[31mERRO: \"{ent}\" é um preço inválido!\033[m')
        else:
            break
    return float(ent)
