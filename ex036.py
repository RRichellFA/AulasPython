casa = float(input('Digite o valor do imóvel: R$'))
sal = float(input('Qual seu salário atual? R$'))
anos = float(input('Em quantos anos você deseja pagar? '))
parcela = anos * 12
valor = sal * 0.3
prest = casa / parcela
if prest > valor:
    print('\033[31mRECUSADO!')
    print('Você não pode pagar mais do que R${:.2f} referente a 30% do seu salário!'.format(valor))
else:
    print('\033[34mAprovado')
print('Você pediu {:.0f} parcelas de R${:.2f}'.format(parcela, prest))
