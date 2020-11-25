def escreva(texto):
    larg = len(texto) + 2
    print('-' * larg)
    print(f' {texto} ')
    print('-' * larg)


escreva(str(input('Texto: ')).strip())
