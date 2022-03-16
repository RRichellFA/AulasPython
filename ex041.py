from datetime import date
nasc = int(input('Digite o ano do nascimento do aluno: '))
idade = date.today().year - nasc
print(idade)
if idade <= 9:
    print('Inscrito na categoria \033[31mMIRIM!')
elif idade <= 14:
    print('Inscrito na categoria \033[32mINFANTIL!')
elif idade <= 19:
    print('Inscrito na categoria \033[34mJUNIOR!')
elif idade <= 25:
    print('Inscrito na categoria \033[35mSÊNIOR!')
elif idade > 25:
    print('Inscrito na categoria \033[36mMASTER!')
