print('Calculo do aumento de salário!')
S = float(input('Qual o salário atual? R$'))
A = float(input('Qual a porcentagem do aumento?'))
V = (S*A)/100
F = S+V
print ('O salário base é de R${:.2f}\nO aumeto foi de {:.2f}%\nO valor aumentado foi de R${:.2f}\nO novo salário é de R${:.2f}'.format(S,A,V,F))
