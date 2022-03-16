dist = int(input('Qual a distância da sua viagem em km? '))
if dist <= 200:
    print('O valor de sua viagem é de R${:.2f}!'.format(dist*0.5))
else:
    print('O valor da sua viagem é de R${:.2f}!'.format(dist*0.45))
