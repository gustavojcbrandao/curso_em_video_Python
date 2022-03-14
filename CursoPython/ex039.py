from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
if anoatual - nascimento == 18:
    print('Você tem {} anos em {} e deve se alistar \033[0:31mIMEDIATAMENTE\033[m!!!'.format(idade, anoatual))
elif anoatual - nascimento < 18:
    print('Você tem {} em {} e ainda faltam {} ano(s) para o seu alistamento'.format(idade, anoatual, 18 - (anoatual - nascimento)))
    print('Seu alistamento será em {}'.format(nascimento + 18))
elif anoatual - nascimento > 18:
    print('Você tem {} anos em {} deveria ter se alistado há {} ano(s)'.format(idade, anoatual, anoatual-(nascimento + 18)))
    print('Seu alistamento foi em {}'.format(nascimento + 18))
