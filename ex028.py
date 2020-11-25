from random import choice
from random import randint
from time import sleep
#método que eu fiz
lista = list(range(1, 6))# lista de numeros dentro do intervalo de posição (valor inclui 0)
c = choice(lista) # escolhe dentro de uma lista
e = int(input('Escolha um número inteiro entre 1 e 5: '))
print('Sorteando...')
sleep(2) #comando para aguardar (segundos)
print('O número escolhido foi {}, o número sorteado foi {}!'.format(e, c))
if c==e:
    print('PARABENS, VOCÊ GANHOU')
else:
    print('Você perdeu, tente denovo.')
#metodo do exercício
comp = randint(1, 5)# gerador de numero inteiro dentro do intervalo
print('O número escolhido foi {} e o sorteado foi {}!'.format(e, comp))
if comp == e:
    print('Voce ganhou')
else:
    print('Você perdeu')
print('Números Válidos:', lista)
