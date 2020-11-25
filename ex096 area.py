def area(a, b):
    c = a * b
    print(f'A área do terreno de {a}m x {b}m é de {c:.2f}m².')


print('-' * 30)
print(f'{"Controle de terrenos":^30}')
print('-' * 30)
x = float(input('Largura (m): '))
y = float(input('Comprimento (m): '))
area(x, y)
