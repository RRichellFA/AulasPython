maior = menor = homem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Maiores de 18 anos: {maior}')
print(f'Sexo Masculino: {homem}')
print(f'Mulheres menores de 20 anos: {menor}')
