print('====== EXERCÍCIO 004 ======')
a = input('Digite o alvo da análise:')
print('O tipo primitivo deste valor é',type(a))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está só em maíuculas?',a.isupper())
print('Está só em minúsculas?',a.islower())
print('Está captitalizada?',a.istitle())