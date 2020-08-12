nome = str(input('Qual é o seu nome? ')).strip().title()
cor = '\033[31m'
if nome == 'Rodrigo':
    cor = '\033[36m'
elif nome in 'Paulo Pedro Gustavo':
    cor = '\033[32m'
print('Tenha um bom dia, {}{}{}!'.format(cor, nome, '\033[m'))
