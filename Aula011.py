"""Estrutura de cores (Padrão ANSI)
\033[style;text;backgroundm
para encerrar a formatação: "\033[m"
Styles - 0  = none
       - 1  = bold
       - 4  = underline
       - 7  = negative

text   - 30 = Branco
       - 31 = Vermelho
       - 32 = Verde
       - 33 = Amarelo
       - 34 = Azul
       - 35 = Roxo
       - 36 = Ciano
       - 37 = Cinza

Back   - 40 = Branco
       - 41 = Vermelho
       - 42 = Verde
       - 43 = Amarelo
       - 44 = Azul
       - 45 = Roxo
       - 46 = Ciano
       - 47 = Cinza"""
nome = str(input('Digite seu nome: '))
#Códigos de formatação dentro do método .format
print('Olá {}{}{}! Prazer em te conhecer.'.format('\033[1;4;31m', nome, '\033[m'))
#Criando uma 'Coleção' com as formatações de cores! (Coleções em aula futura)
cores = {'limpa':'\033[m',
         'verm':'\033[1;31m',
         'fazul':'\033[44m'}
print('Olá {}{}{}{}! Muito Prazer!'.format(cores['fazul'], cores['verm'], nome, cores['limpa']))
