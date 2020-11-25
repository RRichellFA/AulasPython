grupo = []
pessoa = []
max = min = 0
op = 's'
while op != 'n':
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    if max == 0 or pessoa[1] > max:
        max = pessoa[1]
    if min == 0 or pessoa[1] < min:
        min = pessoa[1]
    pessoa.clear()
    op = str(input('Deseja Continuar? [S/N]: ')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Opção Invalida.\nDeseja continuar? [S/N]: '))
print('-=' *30 )
print(f'Foram cadastradas {len(grupo)} pessoas na lista.')
print(f'O Maior peso foi de {max:.1f}Kg. Nomes: ', end='')
for c, v in enumerate(grupo):
    if grupo[c][1] == max:
        print(f'{grupo[c][0]}...', end='')
print(f'\nO menor peso foi de {min:.1f}Kg. Nomes: ', end='')
for c, v in enumerate(grupo):
    if grupo[c][1] == min:
        print(f'{grupo[c][0]}...', end='')
print('\nFim do programa!')
