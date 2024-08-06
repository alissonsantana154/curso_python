""" Calculadora com while """
while True: 
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*); ')

    numero_validos = None
    num_1 = 0
    num_2 = 0

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None: 
        print('Um ou ambos os números digitados são inválido.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1}+{num_2}=', num_1 + num_2)
    elif operador == '-':
        print(f'{num_1}-{num_2}=',num_1 - num_2)
    elif operador == '/':
        print(f'{num_1}/{num_2}=',num_1 / num_2)
    elif operador == '*':
        print(f'{num_1}*{num_2}=',num_1 * num_2)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break