frase = 'curso em vídeo python'
frase2 = '   Aprenda Python  '
lista = [frase, frase2]
print('='*30)
print('Frase analisada:', frase)
print('Mostrar apenas o espaço 11:', frase[11])
print('Mostrar até o espaço 5:', frase[:5])
print('Mostrar a partir do espaço 15:', frase[15:])
print('Mostrar do 9 ao 20 pulando 3 espaços:', frase[9:20:3])
print('Mostrar o numero de caracteres total:', len(frase))
print('Mostrar quantos caracteres especificados >>> o <<< existem no intervalo de 0 ao 13:', frase.count('o', 0, 13))
print('Mostrar o local da parte especificada >>> deo <<<:', frase.find('deo'))
print('Mostrar posição de string inexistente >>> Android <<<:', frase.find('Android'))
print('Existência de str na frase >>> Curso <<<:', 'Curso' in frase)
print('Substituição de str >>> Python, Android <<<:', frase.replace('Python', 'Android'))
print('Mostrar em maiuscula e contar os >>> O <<<:', frase.upper(), frase.upper().count('O'))
print('Mostrar em minúscula e contar os >>> v <<<:',frase.lower(), frase.lower().count('v'))
print('Apenas a primeira em maiúscula:', frase.capitalize())
print('A primeira letra de cada palavra em maiúscula:', frase.title())
print('Dividir as palavras em str diferentes e criar uma lista de palavras sem os espaços:', frase.split())
print('='*100)
print('Frase analisada:', frase2 + '.')
print('Remover espaços inúteis:', frase2.strip() + '.')
print('Remover espaços a direita:', frase2.rstrip()+'.')
print('Remover espaços a esquerda:', frase2.lstrip()+'.')
print('='*100)
print('Juntar str diferentes com a configuração específica >>> --- <<<:', '---'.join(lista))
print('='*100)
print('Imprimindo um texto inteiro usando 3 aspas duplas:')

print("""Quando começamos a programar, uma das principais dúvidas de iniciantes é:
"qual ferramenta vou utilizar para escrever código?". A maioria dos códigos
das principais linguagens de programação permitem desenvolver em um arquivo
utilizando um editor de texto comum.
Alguns editores de texto possuem ferramentas mais sofisticadas que dão maior
auxílio na hora de desenvolver como: indentação de código, diferenciação de
funções, autocompletamento de código, dentre outras.""")
