while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador(+ - / *): ')

    numero_1_valido = None
    numero_2_valido = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        numero_1_valido = True
    except:
        numero_1_valido = None
    try:
        num_2_float = float(numero_2)
        numero_2_valido = True
    except:
        numero_2_valido = None

    if numero_1_valido is None:
        print('O primeiro número é inválido')
        continue

    if numero_2_valido is None:
        print('O segundo número é inválido')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando a sua conta, confira o resultado abaixo: ')
    
    if operador == '+':
        print(f'O número {num_1_float} somado ao número {num_2_float} resulta em: ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'O número {num_1_float} subtraindo o número {num_2_float} resulta em: ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'O número {num_1_float} dividido por {num_2_float} resulta em: ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'O número {num_1_float} multiplicado por {num_2_float} resulta em: ', num_1_float * num_2_float)
    else:
        print('Essa mensagem nunca deveria aparecer')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break