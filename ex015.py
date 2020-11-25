d = int(input('Digite o número de dias que o carro ficou alugado: '))
km = float(input('Digite o número de Km rodados: '))
total = (d*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(total))
