def voto(nasc):
    """
    Calcula se a pessoa pode/deve ou não votar esse ano
    :param nasc: Ano de nascimento
    :return: Strings 'Negado', 'Opcional', 'Obrigatório'
    """
    from datetime import date # Economiza memória, pois só usa o import dentro da chamada da funcao
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: Não VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL!'
    else:
        return f'Com {idade} anos: Voto OBRIGATÓRIO!'


ano = int(input('Digite o seu ano de nascimento: '))
print(f'{voto(ano)}')
