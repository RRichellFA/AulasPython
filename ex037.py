num = int(input('Escreva um número inteiro qualquer: '))
print("""[ 2 ] BINÁRIO!
[ 8 ] OCTAL
[ 16 ] HEXADECIMAL""")
base = int(input('Escolha a base numérica de conversão: '))
if base == 2:
    print('{} convertido para base BINÁRIA é igual a {}'.format(num, bin(num)[2:]))
elif base == 8:
    print('{} convertido para base OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 16:
    print('{} convertido para base HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida, por favor escolha uma base de conversão da lista!\033[m')
