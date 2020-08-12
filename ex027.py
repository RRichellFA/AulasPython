nome = str(input('Digite seu nome completo:')).title().strip()
NOME = nome.split()
print('Olá {} {}! Seja bem vindo.'.format(NOME[0], NOME[-1]))
print('Olá {} {}! Seja bem vindo.'.format(NOME[0], NOME[len(NOME)-1]))
