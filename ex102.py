def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: Parametro obrigatório, Número a ser fatorado.
    :param show: Parametro lógico opcional, se True, mostra o processo de fatoração do número.
    :return: Retorna o valor do numero ja fatorado!
    """
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    if show:
        print('O processo é...')
        for c in range(numero, 0, -1):
            if c == 1:
                print(f'{c}', end='')
            else:
                print(f'{c} x ', end='')
        print(f' = {f}')
    return f


help(fatorial)
num = int(input('Digite um valor a ser fatorado: '))
op = str(input('Deseja mostrar o processo do calculo? ')).strip()[0]
if op in 'sS':
    fat = fatorial(num, True)
else:
    fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
