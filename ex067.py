print('PROGRAMA TABUADA 3.0')
print('Para encerrar digite um valor negativo!')
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    print('-' * 20)
    if valor >= 0:
        for c in range(1, 11):
            print(f'{valor} x {c} = {valor*c}')
    else:
        break
    print('-'*20)
print('Programa TABUADA encerrado!')
