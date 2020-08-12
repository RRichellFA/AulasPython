n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
lista = [n1, n2, n3]
#forma simples
print('Maior: {}, menor: {}!'.format(max(lista), min(lista)))
#forma muito grande
if n1 > n2 > n3:
    print('O maior é {} e o menor é {}!'.format(n1, n3))
if n1 > n3 > n2:
    print('O maior é {} e o menor é {}!'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior é {} e o menor é {}!'.format(n2, n3))
if n2 > n3 > n1:
    print('O maior é {} e o menor é {}!'.format(n2, n1))
if n3 > n1 > n2:
    print('O maior é {} e o menor é {}!'.format(n3, n2))
if n3 > n2 > n1:
    print('O maior é {} e o menor é {}!'.format(n3, n1))
