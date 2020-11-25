from math import cos,sin,tan, radians
ang = float(input('Digite um angulo qualquer: '))
print('Ângulo: {:.2f}\nSeno: {:.2f}\nCoseno: {:.2f}\nTangente: {:.2f}'.format(ang,sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))
