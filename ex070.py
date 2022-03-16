mil = total = menor = cont = 0
prod = ' '
while True:
    nome = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: '))
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        prod = nome
    if preco > 1000:
        mil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R${total:.2f}')
print(f'{mil} produtos custaram mais de mil reais!')
print(f'O produto mais barato é {prod} no valor de R${menor:.2f}!')
