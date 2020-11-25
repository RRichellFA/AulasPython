ini = int(input('Digite o valor inicial da PA: '))
raz = int(input('Digite a razão da PA: '))
cont = 0
print(ini, end=' -> ')
while cont < 9:
    ini += raz
    cont += 1
    print(ini, end=' -> ')
print('FIM')
