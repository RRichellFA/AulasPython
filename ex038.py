n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
if n1 == n2:
    print('\033[31mOs valores {} e {} são iguais!'.format(n1, n2))
elif n1 > n2:
    print('\033[32m{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[34m{} é maior que {}'.format(n2, n1))
