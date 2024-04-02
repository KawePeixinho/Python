while True:
    number_one = input('digite o primeiro número: ')
    number_two = input('digite o segundo número: ')
    operador = input('digite um dos operadores ( + - * / ): ')

    number_ok = None

    try:
        one_float = float(number_one)
        two_float = float(number_two)
        number_ok = True
    except:
        number_ok = False

    if number_ok is False:
        print('um ou ambos os números digitados são inválidos')
        continue

    operadores = '+-*/'

    if operador not in operadores:
        print('Operador Inválido')
        continue

    if len(operador)>1:
        print('foi digitado mais de um operador')
        continue

    if operador == '+':
        resultado = one_float + two_float
        print(f'O resultado de {one_float} {operador} + é: {resultado}')

    elif operador == '-':
        resultado = one_float - two_float
        print(f'O resultado de {one_float} {operador} - é: {resultado}')
    
    elif operador == '*':
        resultado = one_float * two_float
        print(f'O resultado de {one_float} {operador} * é: {resultado}')

    else:
        resultado = one_float / two_float
        print(f'O resultado de {one_float} {operador} / é: {resultado}')

    sair =input('Deseja [s]air? ').lower().startswith('s')

    if sair is True:
        print('\nFim')
        break