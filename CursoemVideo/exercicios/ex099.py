def maior(* valores):
    print('='*50)
    print(f'Foram passados {len(valores)} valores.')
    maior = 0
    for index, val in enumerate(valores):
        print(val, end=' ')
        if index == 0:
            maior = val
        else:
            if val > maior:
                maior = val
    print()
    print(f'O maior é {maior}.')


maior(10, 55, 29, 80, 99, 103, 3218321)
maior(1, 2, 3, 55, 6, 7, 8)
maior(6)
maior()
