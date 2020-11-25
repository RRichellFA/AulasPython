lista = []
for n in range(1, 6):
    peso = float(input('Insira o peso da pessoa {}: '.format(n)))
    lista.append(peso)
print('A pessoa mais pesada pesa {:.1f} Kg, e a mais leve pesa {:.1f} kg.'.format(max(lista), min(lista)))
