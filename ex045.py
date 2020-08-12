from random import randint
print('-='*50)
print("""Vamos jogar "Pedra, Papel, Tesoura, Lagarto, Spock"
Regras: Escolha entre as opções:

1 = Pedra     2 = Papel
3 = Tesoura   4 = Lagarto
       5 = Spock

O computador irá escolher uma opção aleatória também. Ganha quem escolher a opção que vence
o adversário seguindo a tabela a baixo:
Tesoura (3) -   corta   - (2) papel.
Papel   (2) -   cobre   - (1) pedra.
Pedra   (1) -   esmaga  - (4) lagarto.
Lagarto (4) -  envenena - (5) Spock.
Spock   (5) -   quebra  - (3) tesoura.
Tesoura (3) -  decapita - (4) lagarto.
Lagarto (4) -    come   - (2) papel.
Papel   (2) -   refuta  - (5) Spock.
Spock   (5) -  vaporiza - (1) pedra.
Pedra   (1) -   amassa  - (3) tesoura.
Vamos Começar!""")
print('-='*50)
p1 = int(input('Digite sua escolha: '))
cpu = randint(1, 5)
lista = ('Oi', 'Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
win = '\033[1;32mPARABÉNS! VOCÊ GANHOU!\033[m'
lose = '\033[31mVOCÊ PERDEU. VIDA LONGA E PRÓSPERA!'
print('Você escolheu {} e o computador escolheu {}!'.format(lista[p1],lista[cpu]))
if p1 == cpu:
    print('\033[7;30mEMPATE! Vamos denovo?\033[m')
elif p1 == 1:
    if cpu == 4 or cpu == 3:
        print(win)
    elif cpu == 2 or cpu == 5:
        print(lose)
elif p1 == 2:
    if cpu == 1 or cpu == 5:
        print(win)
    elif cpu == 4 or cpu == 3:
        print(lose)
elif p1 == 3:
    if cpu == 2 or cpu == 4:
        print(win)
    elif cpu == 1 or cpu == 5:
        print(lose)
elif p1 == 4:
    if cpu == 2 or cpu == 5:
        print(win)
    elif cpu == 1 or cpu == 3:
        print(lose)
elif p1 == 5:
    if cpu == 1 or cpu == 3:
        print(win)
    elif cpu == 2 or cpu == 4:
        print(lose)
elif p1 == 0 or p1 >5:
    print('Você não escolheu uma opção válida! Tente denovo.')
