lista = []
somaid = 0
op = 's'
while op != 'n':
    pessoa = {"Nome": str(input("Nome: ")).strip().capitalize(),
              "Sexo": str(input("Sexo (M/F): ")).strip().upper()[0],
              "Idade": int(input("Idade: "))}
    lista.append(pessoa.copy())
    somaid += pessoa["Idade"]
    op = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
    while op not in 'sn':
        op = str(input("Opção Inválida, por favor escolha S ou N!\n Deseja Continuar? ")).strip().lower()[0]
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('As mulheres cadastradas: ', end='')
for p in range(len(lista)):
    if lista[p]["Sexo"] == "F":
        print(f'{lista[p]["Nome"]}... ', end='')
print()
print('-=' * 30)
print(f'A média das Idades cadastradas é {somaid / len(lista)}.')
print('As pessoas com idade acima da média são:')
for v in range(len(lista)):
    if lista[v]["Idade"] > somaid / len(lista):
        print(f'Nome: {lista[v]["Nome"]}, Sexo: {lista[v]["Sexo"]}, Idade: {lista[v]["Idade"]}')
