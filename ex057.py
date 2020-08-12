sexo = 'k'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Por favor, escolha uma opção válida!')
print('Obrigado!')
