def fatorial(num):
    f = 1
    for n in range(num, 0, -1):
        f *= n
    return f