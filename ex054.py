from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for nome in range(1, 8):
    ano = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(nome)))
    if hoje - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Existem \033[33m{}\033[m pessoas maiores de idade e \033[31m{}\033[m pessoas menores de idade!'.format(maior, menor))
