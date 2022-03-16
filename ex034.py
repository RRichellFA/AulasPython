sal = float(input('Digite o seu salário atual: R$'))
if sal > 1250:
    print('O seu aumento será de R${:.2f} e seu salário atualizado é de R${:.2f}!'.format(sal*0.1, sal+(sal*0.1)))
else:
    print('O seu aumento será de R${:.2f} e seu salário atualizado é de R${:.2f}!'.format(sal*0.15, sal+(sal*0.15)))
