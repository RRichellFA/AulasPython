lista = []
op = 'S'
while op != 'N':
    val = int(input('Digite um valor: '))
    if val not in lista:
        print('Valor adicionado!')
        lista.append(val)
    else:
        print('Valor duplicado não adicionado!')
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Por favor digite uma opção valida!\n'
                       'Deseja contnuar? [S/N]: ')).strip().upper()[0]
lista.sort()
print(f'A lista dos valores adicionados em ordem crescente é {lista}.')
