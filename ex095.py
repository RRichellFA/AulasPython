time = []
op = 's'
while op != 'n':
    jogador = {"Nome": str(input('Nome: ')).strip().capitalize(),
               "Partidas": int(input("Quantas partidas ele jogou? "))}
    partidas = []
    for p in range(jogador["Partidas"]):
        partidas.append(int(input(f"Quantos gols ele fez na {p+1}ª partida? ")))
    jogador["Jogos"] = partidas[:]
    jogador["Gols"] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    del jogador
    op = str(input("Deseja Continuar? [S/N] ")).strip().lower()[0]
    while op not in 'sn':
        op = str(input("Opção inválida, por favor escolha S ou N.\nDeseja Continuar? ")).strip().lower()[0]
print(time)
print("-=" * 30)
print(f'{"Tabela do time":-^40}')
print(f'{"cod":4}{"Nome":15}{"Gols":15}{"Total":6}')
for p in range(len(time)):
    print(f'{p:<4}{time[p]["Nome"]:15}{str(time[p]["Jogos"]):15}{time[p]["Gols"]:5}')
print("-=" * 30)
while True:
    user = int(input("Você gostaria dos dados de qual jogador?\n(digite o código) (999 para interromper)>>> "))
    while user not in range(len(time)) and user != 999:
        user = int(input("Por favor, escolha um jogador na lista.\nGostaria dos dados de qual jogador?\n>>> "))
    if user == 999:
        break
    print(f'Levantamento do jogador {time[user]["Nome"]}.')
    for c, v in enumerate(time[user]["Jogos"]):
        print(f'No jogo {c+1} ele fez {v} gols!')
    print('-' * 30)
print("FIM DO PROGRAMA!")
