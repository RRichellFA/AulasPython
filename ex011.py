print('Cálculo para a pintura de uma parede!')
h = float(input('Qual a altura da parede a ser pintada (em centimetros)?'))
l = float(input('Qual a largura da parede a ser pintada (em centimetros)?'))
a = (h/100)*(l/100)
t = a/2
print ('A altura da parede é de {:.2f}m\n'
       'A largura é de {:.2f}m\n'
       'A área total a ser pintada é de {:.2f}m²\n'
       'A quantidade de tinta necessária é de {:.2f}l'.format(h/100, l/100, a, t))
