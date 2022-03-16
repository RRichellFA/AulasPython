from random import randint
cpu = randint(0, 10)
user = 20
cont = 0
while cpu != user:
    user = int(input('Escolha um número inteiro entre 0 e 10: '))
    print('Você escolheu {} e o computador escolheu {}!'.format(user, cpu))
    cont += 1
    if user != cpu:
        print('Você \033[31merrou\033[m, tente denovo!')
        cpu = randint(0, 10)
        user = 20
print('\033[33mParabéns\033[m, você acertou depois de {} tentativas!'.format(cont))
