from math import hypot
print('Calculo da hipotenusa de um triangulo retangulo!')
cata = float(input('Digite o comprumento do cateto a: '))
catb = float(input('Digite o comprimento do cateto b: '))
# hip = ((cata**2)+(catb**2))**(1/2)
# print('A hipotenusa deste triangulo é igual a {}'.format(hip))
print('A hipotenusa deste triangulo é igual a {}'.format(hypot(cata, catb)))
