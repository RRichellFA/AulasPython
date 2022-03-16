from datetime import date
nasc = int(input('Digite o ano de seu nascimento: '))
Idade = date.today().year-nasc
print(Idade)
if Idade == 18:
    print('\033[34mVocê deve se apresentar para alistamento!')
elif Idade < 18:
    print('\033[32mFaltam {} anos para você se alistar!'.format(18-Idade))
elif Idade > 18:
    print('\033[31mVocê deveria ter se alistado em {}!'.format(nasc+18))
