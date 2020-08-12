# --- Funções def()---
# Funções são rotinas para serem utilizadas dentro do programa
# Quando definindo uma rotina:
# Sintaxe:
# def função(parametros):
#     Rotina que será utilizada sempre que a função for chamada
# A estética pede que tenha 2 linhas de diferença entre a definição de função e as outras linhas
# Exenplos:
print('*** Exemplo 1 ***')


def mostralinha():  # definindo a rotina
    print('-' * 30)


mostralinha()  # chamando a função definida
print()
print('*** Exemplo 2 ***')


def titulo(texto):  # definindo a rotina com parametros
    print('-' * 30)
    print(f'{texto:^30}')  # usando o parametro inserido
    print('-' * 30)


titulo('Titulo exemplo!')  # chamando a função com o parametro
print()
print('*** Exemplo 3 ***')


def soma(a, b):  # definindo a rotina com parametros
    print(f'Valor de a = {a} e Valor de b = {b}')
    print(f'A soma de a+b é {a + b}')  # trabalhando com os parametros


soma(1, 2)  # chamando a função no formato padrão
soma(b=5, a=3)  # chamando a função especificando os parametros
print()
print('*** Exemplo 4 ***')


def somatodos(* num):  # o * pega todos os parametros passados e joga dentro da tupla num
    print(num)  # mostrando todos os parametros empacotados, eles são organizados em uma tupla!
    print(sum(num))  # Somando todos os parametros inseridos
    for valor in num:  # tudo que puder ser feito com uma tupla, pode ser feito com os parametros empacotados!
        print(f'{valor} ', end='')
    print()
    for v, n in enumerate(num):
        print(f'O campo {v} é {n}!')
    print(f'Recebi o valores {num} que são ao todo {len(num)} numeros.')
    print()


somatodos(1, 2, 3, 4) # chamando a função com 4 parametros
somatodos(2, 3)  # chamando a função com 2 parametros
somatodos(3, 4, 5)  # chamando a função com 3 parametros
print('*** Exemplo 5 ***')
valores = [7, 2, 5, 0, 4]
print(valores)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1
    print(lista)


dobra(valores)
print('*** FIM! ***')
