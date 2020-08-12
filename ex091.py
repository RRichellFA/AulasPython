from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
max = 0
jogo['Jogador 1'] = randint(1, 6)
jogo['Jogador 2'] = randint(1, 6)
jogo['Jogador 3'] = randint(1, 6)
jogo['Jogador 4'] = randint(1, 6)
print('Os jogos tirados foram:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    if v >= max:
        max = v
    sleep(0.5)
print('O Ranking dos jogadores foi:')
for k, v in sorted(jogo.items(), key=itemgetter(1), reverse=True):
    print(f'{k} com {v}')
    sleep(0.5)
print('O jogador vencedor foi: ')
for c, v in jogo.items():
    if v == max:
        print(c, end=' ')
print()
print(jogo)
print(max)