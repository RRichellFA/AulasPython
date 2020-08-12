from time import sleep
from random import randint
todos = []
jogos = []
user = int(input('Quantos jogos da Mega sena deseja sortear? '))
numeros = int(input('Quatos números deseja sortear por jogo? :'))
while len(todos) != user:
    while len(jogos) != numeros:
        num = randint(0, 60)
        if num not in jogos:
            jogos.append(num)
    jogos.sort()
    todos.append(jogos[:])
    jogos.clear()
print('-=' * 18)
print(f'{f" Sorteando {user} jogos. ":^36}')
for c, v in enumerate(todos):
    print(f'O jogo {c+1} é {todos[c]}')
    sleep(1)
print('-=' * 18)
print(f'{"Fim do programa":*^36}')
