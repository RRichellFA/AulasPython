m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('Seguindo a matriz a seguir')
print('*' * 30)
print("""
    0    1    2
0 [   ][   ][   ]
1 [   ][   ][   ]
2 [   ][   ][   ]
""")
print('*' * 30)
print('Insira os valores correspondentes as seguintes posições.')
for l in range(3):
    for c in range(3):
        m[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
print('*' * 30)
print('A matriz estabelecida foi...')
for l in range(3):
    for c in range(3):
        print(f'[{m[l][c]:^5}]', end='')
    print()
print(f'\n{" Fim do programa ":*^30}')
