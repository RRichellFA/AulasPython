from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Não foi passado nenhum número.')
    else:
        for valor in num:
            print(f'{valor} ', end='')
            sleep(0.3)
        print()
        print(f'Foram passados {len(num)} números.')
        print(f'O maior valo foi {max(num)}')


maior(5, 4, 9, 1, 5)
maior(3, 4, 5)
maior(6)
maior()