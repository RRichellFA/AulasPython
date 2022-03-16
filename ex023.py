num = int(input('Digite um número inteiro entre 0 e 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 100000000000000000000000
print('Analizando o número {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhares:{}'.format(m))
#EU ERREI E COLEI A RESPOSTA
