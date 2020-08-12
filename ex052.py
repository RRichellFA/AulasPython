v = int(input('Digite um número inteiro: '))
p = 0
for c in range(1, v+1):
    if v % c == 0:
        p += 1
print('O número {} foi divisivel {} vezes!'.format(v, p))
if p == 2:
    print('\033[33mÉ PRIMO!')
else:
    print('\033[31mNÃO É PRIMO!')
