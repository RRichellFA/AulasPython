aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Media'] = float(input('Mádia: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f"{k} = {v}")
