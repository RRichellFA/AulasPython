brasileirao = ('Botafogo', 'Bahia', 'Gremio', 'Athletico-PR', 'Bragantino-SP', 'Fortaleza', 'Santos', 'Vasco da gama',
               'Atlético-GO', 'Corinthians', 'Palmeiras', 'São Paulo', 'Flamengo', 'Coritiba', 'Atlético-MG', 'Goiás',
               'Ceará SC', 'Fluminense', 'Internacional', 'Sport Recife')
divisa = "-=" * 50
print(divisa)
print(f'{"Estatísticas do Brasileirão":^100}')
print(divisa)
print(f'Os primeiros 5 colocados são {brasileirao[:5]}!')
print(divisa)
print(f'Os últimos 4 colocados são {brasileirao[-4:]}!')
print(divisa)
print(f'Os 20 primeiros em órdem alfabética são'
      f'\n{sorted(brasileirao[:5])}'
      f'\n{sorted(brasileirao[5:10])}'
      f'\n{sorted(brasileirao[10:15])}'
      f'\n{sorted(brasileirao[15:])}!')
print(divisa)
print('Somos todos Chapecoenses!')
print(divisa)
print(f"O Corinthians está na {brasileirao.index('Corinthians')+1}ª posição!")
