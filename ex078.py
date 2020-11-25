lista = []
for c in range(5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'O MAIOR valor encontrado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f'O MENOR valor encontrado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
