soma = 0
cont = 0
for c in range(1, 7):
    v = int(input('Digite {}º valor: '.format(c)))
    if v % 2 == 0:
        soma += v
        cont += 1
print('{} números são pares e a soma deles é {}!'.format(cont, soma))
