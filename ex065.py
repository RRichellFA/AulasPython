soma = 0
cont = 0
parar = 'N'
while parar == 'N':
    num = int(input('Digite o {}º valor: '.format(cont+1)))
    parar = str(input('Deseja parar? [S/N]: ')).strip().upper()
    soma += num
    cont += 1
print(f'A média entre os {cont} valores é de {soma/cont}!')
