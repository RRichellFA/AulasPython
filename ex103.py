def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


nome = str(input('Nome: ')).strip().capitalize()
gols = input('Gols: ')
if nome == '':
    if gols == '':
        ficha()
    else:
        gols = int(gols)
        ficha(gols=gols)
else:
    if gols == '':
        ficha(nome=nome)
    else:
        gols = int(gols)
        ficha(nome=nome, gols=gols)
