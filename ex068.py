from random import randint
print('Vamos jogar "PAR ou IMPAR"!')
cont = 0
while True:
    print('-='*30)
    PI = str(input('Escolha PAR ou IMPAR [P/I]: ')).strip().upper()
    user = int(input('Digite um valor: '))
    cpu = randint(0, 11)
    soma = user + cpu
    if PI == 'P':
        if soma % 2 == 0:
            print(f'Você escolheu {user} a CPU escolheu {cpu} e a soma foi {soma}!')
            print('Parabéns, você venceu! Vamos denovo...')
            cont += 1
        else:
            break
    if PI == 'I':
        if soma % 2 != 0:
            print(f'Você escolheu {user} a CPU escolheu {cpu} e a soma foi {soma}!')
            print('Parabéns, você venceu! Vamos denovo...')
            cont += 1
        else:
            break
print(f'Você escolheu {user} e a CPU escolheu {cpu}, a soma foi de {soma}')
if cont == 0:
    print('Que pena, você perdeu na primeira!')
else:
    print(f'Que pena você perdeu depois de {cont} vitórias consecutivas!')
