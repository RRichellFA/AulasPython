compras = ('Lapiz', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 25,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
print('*' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('*' * 40)
for n in range(0, len(compras), 2):
    print(f'{compras[n]:.<31}R$ {compras[n+1]:>6.2f}')
print('*' * 40)
