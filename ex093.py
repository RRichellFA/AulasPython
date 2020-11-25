jogador = {"Nome": str(input('Nome do jogador: ').strip().capitalize())}
Partidas = int(input("Quantas partidas ele jogou? "))
partidas = []
for p in range(Partidas):
    partidas.append(int(input(f'Na {p+1}ª partida ele fez quantos gols? ')))
jogador["Jogos"] = partidas
jogador["Gols"] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items():
    print(f'{key}: {value}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {Partidas} partidas!')
for p in range(len(partidas)):
    print(f' '*4, f'==>Na {p+1}ª partida ele fez {partidas[p]} gols!')
print(f'{jogador["Nome"]} fez no total {jogador["Gols"]} gols')
