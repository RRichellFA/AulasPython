user = input('Escreva uma frase: ').strip().upper().split()
junto = ''.join(user)
inverso = junto[::-1]
print('Normal:   ', junto)
print('Invertido:', inverso)
if junto == inverso:
    print('\033[33mÉ um palíndromo')
else:
    print('\033[31mNão é um palíndromo')
