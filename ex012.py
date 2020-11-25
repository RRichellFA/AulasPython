print('Calculo do desconto de um produto!')
P = float(input('Qual o valor do produto?'))
D = float(input('Qual a porcentagem do desconto?'))
e = (P*D)/100
v = P-e
print('O valor original do produto é R${:.2f}\nO desconto é de {:.1f}%\nVocê economizou R${:.2f}\nO valor do produto com desconto é de R${:.2f}'.format(P,D,e,v))
