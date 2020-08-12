# listas compostas
# pedro = ['Pedro', 25, 'M']
# maria = ['Maria', 19, 'F']
# joao = ['João', 32, 'M']
# pessoas = [pedro, maria, joao]
# print(pessoas)

# não esquecer que sem o [:], ele vincula as duas listas!
# teste = []
# teste.append('Gustavo')
# teste.append('40')
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# Declarar a lista já dentro da lista... Buscar dados dentro da lista!
# galera = [['João', 19, 'Homem'], ['Ana', 33, 'Mulher'], ['Joaquim', 13, 'Homem'], ['Maria', 45, 'Mulher']]
# for pessoa in galera:
#     print(f'{pessoa[0]} é {pessoa[2]} e tem {pessoa[1]} anos de idade!')

# coletando dados e armazenando em uma lista composta
# galera = []
# dados = []
# maior = menor = 0
# for c in range(4):
#     dados.append(str(input('Nome: ')).strip().capitalize())
#     dados.append(int(input('Idade: ')))
#     dados.append(str(input('Sexo [M/F]:')).upper()[0])
#     galera.append(dados[:])
#     dados.clear()
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade e é do sexo ',end='')
#     print(f'Masculino.' if p[2] == 'M' else 'Feminino.')
#     if p[1] >= 18:
#         print(f'{p[0]} é maior de idade!')
#         maior += 1
#     else:
#         print(f'{p[0]} é menor de idade!')
#         menor += 1
# print(f'{maior} pessoas são maiores de idade.\n'
#       f'{menor} pessoas são menores de idade.')
