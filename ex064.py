num = soma = cont = 0
print('Insira os numeros inteiros que deseja. Para sair insira [999]!')
while True:
    num = int(input('--→  '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores indicados é de {soma}!')
