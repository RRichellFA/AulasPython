from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 9))
    print('Os valores sorteados foram: ', end='')
    for v in lista:
        print(f'{v} ', end='')
    print('FIM')


def somapar(lista):
    soma = 0
    print('Os valores pares sorteados foram: ', end='')
    for valor in lista:
        if valor % 2 == 0 and valor > 0:
            print(f'{valor} ', end='')
            soma += valor
    print()
    print(f'A soma dos valores pares do sorteio é {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
