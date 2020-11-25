ini = int(input('Digite o valor inicial da PA: '))
raz = int(input('Digite a razão da PA: '))
cont = 0
top = 10
menu = 0
print(ini, end=' → ')
while cont < top:
    ini = ini + (raz)
    cont += 1
    print(ini, end=' → ')
    if cont == (top-1):
        menu = int(input('Gostaria de mais quantos valores? [0] para encerrar: '))
        if menu != 0:
            top += menu
        else:
            break
print('FIM')
