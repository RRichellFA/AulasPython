# dicionario = dict()
# lista = list()
# tupla = tuple()

# dicionário = {'key':'value', 'key':'value'}
#                   Item   ,       Item
# ********************************************************************
# filme = {'Titulo': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}
# for key, value in filme.items():
#     print(f'O {key} é {value}.')
#
# O [Titulo] é [Star Wars].
# O [Ano] é [1977].
# O [Diretor] é [George Lucas].
# ********************************************************************
# pessoas = {'Nome': 'Rodrigo', 'Sexo': 'Masculino', 'Idade': 36}
# print(pessoas['Nome'])
# print(pessoas['Sexo'])
# print(pessoas['Idade'])
# print('-='*30)
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
# print('-='*30)
# print(pessoas.keys())
# print(pessoas.items())
# print(pessoas.values())
# print('-='*30)
# for key in pessoas.keys():
#     print(key)
# for value in pessoas.values():
#     print(value)
# for item in pessoas.items():
#     print(item)
# print('-='*30)
# pessoas['Nome'] = 'Leandro'
# pessoas['Peso'] = 90
# for key, value in pessoas.items():
#     print(f'{key} = {value}')
# print('-='*30)
# *************************************************
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])
# **************************************************
# estado = dict()
# brasil = list()
# for c in range(3):
#     estado['uf'] = str(input('Unidade Federativa: ')) # Adicionando Keys e valores ao dicionário
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado.copy()) # Copiar dicionário sem vincular
# print(brasil)
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()
