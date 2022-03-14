nome = str(input('Qual é o seu nome completo? ')).strip().lower().split()
teste = 'silva' in nome
print('Seu nome tem silva? {}'.format(teste))