print('-='*13)
print('Vamos analizar triangulos')
print('-='*13)
l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))
lista = [l1, l2, l3]
if max(lista) > sum(lista)-max(lista):
    print('Estes valores não formam um triangulo!')
else:
    print('Estes valores formam um triangulo!')
