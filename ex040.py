n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação:  '))
n3 = float(input('Nota da terceira avaliação: '))
n4 = float(input('Nota da quarta avaliação:   '))
m = (n1+n2+n3+n4)/4
print('Sua média foi...')
if m < 5:
    print('{:.1f}, \033[31mREPROVADO!'.format(m))
elif 5 <= m < 7:
    print('{:.1f}, \033[32mRECUPERAÇÃO'.format(m))
elif m >= 7:
    print('{:.1f}, \033[34mAPROVADO'.format(m))
