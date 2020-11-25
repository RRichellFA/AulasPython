vel = float(input('Velocidade do carro em Km/h: '))
print('Limite de Velocidade: 80 km/h.')
print('Multa de R$ 7.00 para cada km/h acima do limite.')
print('A velocidade detectada foi de {:.2f} km/h.'.format(vel))
if vel>=80:
    print('Você ultrapassou o limite de velocidade.')
    print('Seu carro foi multado em R${:.2f}.'.format((vel-80)*7))
print('Tenha um bom dia! Dirija com segurança!')