# AULA 010 - CONDIÇÕES
# EXEMPLO 01 - Comandos de condições e blocos!
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
# EXEMPLO 02 - CONDIÇÃO SIMPLIFICADA
print('Carro novo'if tempo <=3 else 'Carro velho!')
print('--FIM--')
# EXEMPLO 03 - PRÁTICA!
nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Rodrigo':
    print('Bom dia Senhor!')
else:
    print(f'Seja bem vindo, {nome}!')
# EXEMPLO 04 - PRÁTICA!
n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
n3 = float(input('Nota da terceira avaliação: '))
n4 = float(input('Nota da quarta avaliação: '))
m = (n1+n2+n3+n4)/4
print(f'A sua média foi de {m:.1f}!')
print('Você passou de ano!' if m >=5 else 'Você reprovou')
