from datetime import date
dados = {"Nome": str(input('Nome: ')).strip().capitalize(),
         "Idade": date.today().year - int(input('Ano de nascimento: ')),
         "Ctps": int(input('CTPS: (0 se não possuir):'))}
if dados["Ctps"] != 0:
    dados["Contratação"] = int(input('Ano da contratação: '))
    dados["Salário"] = f"R$ {float(input('Salário: R$ '))}"
    dados["Aposentadoria"] = ((dados["Contratação"]+35) - (date.today().year - dados["Idade"]))
print("-=" * 30)
print(dados)
for key, value in dados.items():
    print(f'{key} é {value}')
