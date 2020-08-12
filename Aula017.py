# ----------PARTE 1----------
# num = [2, 5, 9, 1]
# num[2] = 3  # substituindo um valor da lista [pos] = valor
# num.append(7)  # adicionando um valor ao final da lista (valor)
# num.sort()  # organizando a lista
# num.sort(reverse=True)  # organizando a lista inversamente
# num.insert(2, 2)  # inserindo na posição x o valor y (pos, valor)
# num.pop(2)  # elimina o elemento da lista (pos) - () para eliminar o ultimo elemento
# if 4 in num:
#     num.remove(4)  # elimina o primeiro valor x encontrado na lista (valor)
# else:
#     print('Não achei o número 4!')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')  # mostrando a quantidade de elementos da lista
# ----------PARTE 2----------
# valores = list()  # criando uma lista vazia. Pode ser [] ou list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Este é o final da lista')
# ----------PARTE 3----------
# a = [2, 3, 4, 7]
# b = a  # faz uma ligação entre as 2 listas, alterações em uma afetam a outra
# b = a[:]  # faz uma cópia em 'b' dos valores da lista 'a'. Sem fazer uma ligação entre elas!
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
