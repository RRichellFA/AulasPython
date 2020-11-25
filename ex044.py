print('{:=^40}'.format(' LOJAS RICHELL '))
preço = float(input('Preço do produto: R$'))
print("""[ 0 ] Dinheiro
[ 1 ] Cartão""")
modo = int(input('Modo de pagamento: '))
if modo == 0:
    print('Pagamento em dinheiro. \033[34m10%\033[m de desconto. Total: R${:.2f}'.format(preço*0.9))
elif modo == 1:
    parc = int(input('Digite o número de parcelas: '))
    if parc == 1:
        print('Pagamento a vista no cartão. \033[34m5%\033[m de desconto. Total: R${:.2f}'.format(parc*0.95))
    elif parc == 2:
        print('Pagamento em 2x de R${:.2f} no cartão. Total: R${:.2f}'.format(preço/parc, preço))
    elif parc >= 3:
        print('Pagamento em {}x de R${:.2f} no cartão. \033[31m20%\033[m de juros. Total: R${:.2f}'.format(parc, (preço*1.2)/parc, preço*1.2))
else:
    print('\033[31mMétodo de pagamento inválido!\033[m')
