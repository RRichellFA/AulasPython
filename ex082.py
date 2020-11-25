num = []
op = 's'
while op != 'n':
    val = int(input('Digite um valor: '))
    num.append(val)
    op = str(input('Deseja Continuar? [S/N]: ')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Por favor digite uma opção válida.\nDeseja Continuar? [S/N]: '))
par = []
imp = []
for v in range(len(num)):
    if num[v] % 2 == 0:
        par.append(num[v])
    else:
        imp.append(num[v])
print(f'A lista foi {num}')
print(f'A lista de pares é {par}' if len(par) > 0 else 'Não houveram numeros pares.')
print(f'A lista de impares é {imp}' if len(imp) > 0 else 'Não houveram números ímpares.')
