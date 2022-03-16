num = (int(input('Valor 1 da tupla: ')),
       int(input('Valor 2 da tupla: ')),
       int(input('Valor 3 da tupla: ')),
       int(input('Valor 4 da tupla: ')))
print(f'Você digitou os valores {num} na tupla')
print(f'O número 9 aparece {num.count(9)} vezes na tupla')
if 3 in num:
       print(f'O primeiro 3 foi digitado n {num.index(3)+1}º valor')
else:
       print('Não há nenhum 3 na tupla!')
print('Os valores pares digitados foram ', end='')
for par in num:
       if par % 2 == 0:
              print(f'{par}', end=' ')
