numeros = [[], []]
for num in range(7):
    val = int(input(f'Digite o {num+1}º valor: '))
    if val % 2 == 0:
        numeros[0].append(val)
    else:
        numeros[1].append(val)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os numeros pares foram {numeros[0]}.\n'
      f'Os numeros impares foram {numeros[1]}.')
print(f'{" Fim do programa ":*^60}')
