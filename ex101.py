from datetime import date


def voto(ano):
    pessoa = date.today().year - ano
    print(f'Você tem {pessoa} anos e seu voto é ', end='')
    if 65 > pessoa >= 18:
        print('obrigatório.')
    if 16 <= pessoa < 18 or pessoa >= 65:
        print('opcional.')
    if pessoa < 16:
        print('negado.')


voto(int(input('Digite o ano em que nasceu: ')))
