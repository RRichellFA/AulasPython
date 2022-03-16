op1 = 0
op2 = 0
fun = 0
while fun != 5:
    op1 = float(input('Digite o primeiro Valor: '))
    op2 = float(input('Digite o segundo Valor: '))
    print('''Agora escolha a função dentre as seguintes:
    [1] Somar
    [2] Multiplicar
    [3] Indicar o maior valor
    [4] Escolher novos operadores
    [5] Encerrar aplicação''')
    fun = int(input('--> '))
    if fun == 1:
        print('A soma entre {} e {} é igual a {}!'.format(op1, op2, op1+op2))
    if fun == 2:
        print('O produto entre os valores {} e {} é igual a {}!'.format(op1, op2, op1*op2))
    if fun == 3:
        if op1 > op2:
            print('O maior valor é {}!'.format(op1))
        if op2 > op1:
            print('O maior valor é {}!'.format(op2))
        if op1 == op2:
            print('O valores são iguais!')
    if fun == 4:
        print('Reiniciando programa...')
    if fun > 5:
        print('\033[31mFunção inexistente!\033[m')
print('Encerrando aplicação!')
