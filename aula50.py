"""
Exercício
Exiba os indices da lista
0 Maria
1 Helena
2 Alisson
"""
lista = ['Maria', 'Helena', 'Alisson']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))