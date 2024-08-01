# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# A l i s s o n
#-7-6-5-4-3-2-1
# nome = 'Alisson'
# print(nome[2])
# print(nome[-5])
# print('son' in nome)
# print('zeros' in nome)
# print(10 * '-')
# print('son' not in nome)
# print('zeros' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontra: ')

if encontrar in nome:
    print(f'{encontrar} foi encontrado em {nome}')
else:
    print(f'{encontrar} não foi encontrado em {nome}')