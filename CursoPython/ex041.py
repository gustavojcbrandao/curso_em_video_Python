from datetime import date
nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 14 < idade <= 25:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')
