#Sequencia de Fibonacci
a = 0
b = 1
c = a + b
n = int(input('Digite quantos valores deseja receber: '))
cont = 0
print('0 → 1', end=' → ')
while cont < n:
    print('{}'.format(c), end=' → ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')
