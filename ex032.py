from datetime import date
ano = int(input('Digite o ano que deseja analizar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year #ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bisexto'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))
