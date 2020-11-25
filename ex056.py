idades = 0
IDVelho = 0
HVelho = ''
M20 = 0
for id in range (1, 5):
    print('----{}ª pessoa.----'.format(id))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    idades += i
    if s == 'M' and i > IDVelho:
        IDVelho = i
        HVelho = n
    if s == 'F' and i < 20:
        M20 += 1
print('*'*50)
print('A média das idades é de {} anos.'.format(idades / 4))
print('O homem mais velho é {} e tem {} anos'.format(HVelho, IDVelho))
print('Existem {} mulheres menores de 20 anos!'.format(M20))
