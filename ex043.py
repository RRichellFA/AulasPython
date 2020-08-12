alt = float(input('Digite sua altura (cm): '))
peso = float(input('Digite seu peso (kg): '))
IMC = peso / (alt/100) ** 2
print('{:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= IMC <= 25:
    print('Você está no peso ideal!')
elif 25 < IMC <= 30:
    print('Você está acima do peso!')
elif 30 < IMC <= 40:
    print('Você está obeso!')
elif 40 < IMC:
    print('Você está com obesidade mórbida!')
