print('-'*10, 'Digite os valores da progressão aritimética', '-'*10)
a1 = int(input('Digite o valor inicial: '))
r = int(input('Digite a razão: '))
n = a1 + 10 * r
for c in range(a1, n, r):
    print('{} '.format(c), end='→ ')
print('FIM')
