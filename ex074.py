from random import randint
numeros = tuple(randint(0, 10) for n in range(5))
print(f'Os valores sorteados foram {numeros}!')
print(f'O maior valor é {max(numeros)} e o menor é {min(numeros)}!')
