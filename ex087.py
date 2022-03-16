m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
print('Seguindo a matriz a seguir')
print('*' * 30)
print("""
l\c 0    1    2
0 [   ][   ][   ]
1 [   ][   ][   ]
2 [   ][   ][   ]
""")
print('*' * 30)
print('Insira os valores correspondentes as seguintes posições.')
for l in range(3):
    for c in range(3):
        m[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
        if m[l][c] % 2 == 0:
            pares += m[l][c]
print('*' * 30)
print('A matriz estabelecida foi...')
for l in range(3):
    for c in range(3):
        print(f'[{m[l][c]:^5}]', end='')
    print()
print(f'\n{" Fim do programa ":*^30}')
print(f'A soma de todos os valores Pares é de {pares}.')
print(f'A soma de todos os valores da terceira coluna é de {m[0][2] + m[1][2] + m[2][2]}')
print(f'O maior valor da segunda linha é {max(m[1])}')
print(f'\n{" Fim do programa ":*^30}')
