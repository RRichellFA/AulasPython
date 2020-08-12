# Tópicos da Aula
# Interactive help, docstrings, Argumentos opcionais, Escopo de variaveis,  Retorno de resultados

# Interactive Help
# Função
# Abra o Python Console e digite a função... help()

# print(input.__doc__)
# print('-=' * 30)
# help(input)

# docstring
# é o manual da função criada na função que criamos para ser utilizada na Interactive help


# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra da tela.
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     função criada na para a aula de docstring
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM')


# contador(0, 100, 10)
# help(contador)

# Parametros Opcionais


# def somar(a=0, b=0, c=0):  # se o parametro não receber valor, recebe 0. Todos os parametros podem ser opcionais!
#     """
#     -> Faz a soma dos parametros informados, todos os parametros são opcionais, mas podem ser no máximo 3.
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     Função criada para a aula do CeV
#     """
#     soma = a + b + c
#     print(f'A soma vale {soma}')


# somar(3, 2, 5)
# somar(8, 4)
# somar()
# help(somar)


# Escopo de Variaveis


# def teste():
#     x = 9  # a variavel x é uma variavel local, só funciona dentro da função!
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
#
#
# n = 2  # a variavel n é uma variavel global, funciona para o programa inteiro.
# print(f'No programa principal, n vale {2}')
# teste()


# def funcao():
#     n1 = 4
#     print(f'N1 dentro da função vale {n1}')
#
# n1 = 2
# funcao()
# print(f'N1 fora da função vale {n1}')


# def teste(b):
#     global a  # irei usar a variavel local a como global, ela deixa de ser uma variavel local e passa a ser global.
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
#
# a = 5
# teste(a)
# print(f'A fora vale {a} pois foi definida como global dentro da função')


# retorno de valor


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s  # ele retorna o valor do resultado.
#
#
# defino uma variavel para receber o valor retornado
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
# print(f'Os resultador foram {r1}, {r2} e {r3}')  # customizo minha resposta.


# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')
# print('-=' * 30)
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é {fatorial(n)}')


# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# while True:
#     n = int(input('Digite um número: '))
#     if par(n):
#         print('Par.')
#     else:
#         print('Impar.')