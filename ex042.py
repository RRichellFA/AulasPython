l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
lista = [l1, l2, l3]
if max(lista) < sum(lista)-max(lista):
    if l1 == l2 == l3:
        print('Este é um triângulo equilátero!')
    elif l1 != l2 != l3 != l1:
        print('Este é um triângulo escaleno!')
    else:
        print('Este é um triângulo isosceles!')
else:
    print('Esses lado não formam um triângulo')
