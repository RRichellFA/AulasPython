extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quartorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
ext = range(21)
while True:
    usuario = int(input('Digite um numero entre 0 e 20: '))
    while usuario not in range(21):
        usuario = int(input('Por favor, escolha um numero entre 0 e 20: '))
    print(f'Você digitou o número \033[31m{extenso[usuario]}\033[m!')
    opcao = str(input('Deseja escolher outro? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção invalida, deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('Fim do Programa!')
