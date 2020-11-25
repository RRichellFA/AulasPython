from time import sleep


def contador(ini, fim, pas):
    print(f'Contando de {ini} a {fim} com passo {pas}')
    if pas == 0:
        pas = 1
    if fim < ini and pas > 0:
        pas *= (-1)
    if ini < fim:
        fim += 1
    if fim < ini:
        fim -= 1
    if ini == fim:
        print('Inicio e fim são iguais. Sem contagem!')
    for c in range(ini, fim, pas):
        print(c, end=' ')
        sleep(0.3)
    print()
    print('-=' * 30)


print('-=' * 30)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de definir os parâmetros.')
contador(int(input('Inicio = ')), int(input('Fim = ')), int(input('Passo = ')))
print('FIM DO PROGRAMA')
