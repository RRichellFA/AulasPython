lista = []
op = 's'
while op != 'n':
    val = int(input('Digite um valor: '))
    lista.append(val)
    op = str(input('Deseja Continuar? [S/N]:')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Por favor escolha uma opção valida!\n'
                       'Deseja Continuar? [S/N]:')).strip().lower()[0]
print(f'Foram digitado {len(lista)} números e colocados em uma lista.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {lista}.')
print(f'O valor 5 está presente na lista e foi digitado {lista.count(5)} vezes.' if 5 in lista else
      'Não foram digitados nenhum valor 5 na lista')
