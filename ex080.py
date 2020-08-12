lista = []
for n in range(5):
    val = int(input('Digite um valor: '))
    if n == 0 or val > lista[-1]:
        lista.append(val)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                print(f'Adicionado na posição [{pos}] da lista.')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

# minha solução tosca. huauhauhauhauha
#     if n == 0:
#         lista.append(val)
#         print(f'O valor {val} é o primeiro item [0] da lista.')
#     elif val > lista[0]:
#         if n == 1:
#             lista.append(val)
#             print(f'O valor {val} foi inserido no final [1] da lista.')
#         elif val > lista[1]:
#             if n == 2:
#                 lista.append(val)
#                 print(f'O valor {val} foi inserido no final [2] da lista.')
#             elif val > lista[2]:
#                 if n == 3:
#                     lista.append(val)
#                     print(f'O valor {val} foi inserido no final [3] da lista.')
#                 elif val > lista[3]:
#                     lista.append(val)
#                     print(f'O valor {val} foi inserido ao final [4] da lista.')
#                 else:
#                     lista.insert(3, val)
#                     print(f'O valor {val} foi inserido na posição [3] da lista.')
#             else:
#                 lista.insert(2, val)
#                 print(f'O valor {val} foi inserido na posição [2] da lista.')
#         else:
#             lista.insert(1, val)
#             print(f'O valor {val} foi inserido na posição [1] da lista.')
#     else:
#         lista.insert(0, val)
#         print(f'O valor {val} foi inserido no inicio [0] da lista.')
# print(f'A lista ordenada sem usar o \033[31m.sort()\033[m é {lista}.')
