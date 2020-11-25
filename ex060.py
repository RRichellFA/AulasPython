valor = int(input('Digite um número para descobrir seu fatorial: '))
fator = 1
c = 0
#while valor > 1:
#    fator = fator * valor
#    valor -= 1
#    c += 1
#print('O fatorial de {} é {}'.format(valor+c, fator))

for valor in range(valor, 1, -1):
    fator = fator * valor
print(fator)
print('FIM')
