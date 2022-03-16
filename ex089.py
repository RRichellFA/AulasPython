from time import sleep
lista = []
op = 's'
while op != 'n':
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], m])
    op = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Opção inválida!'
                       'Deseja continuar? [S/N]: ')).strip().lower()[0]
print('-=' * 20)
print('Nº. Nome         Média')
print('-' * 23)
for c, v in enumerate(lista):
    print(f'{c:<4}{v[0]:<15}{v[2]:.1f}')
print('-' * 23)
print('-=' * 20)
while True:
    user = int(input('Gostaria de ver as notas de qual aluno? (999 para interromper): '))
    if user < len(lista):
        print(f'As notas de {lista[user][0]} são {lista[user][1]}.')
    if user >= len(lista) and user != 999:
        print('Aluno não encontrado!')
    if user == 999:
        print('Encerrando...')
        sleep(1)
        break
print('Fim do Programa!')
