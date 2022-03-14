from random import randint
c = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que vc consegue adivinhar qual foi?')
user = int(input('Qual é o seu palpite? '))
n = randint(0, 1)
if n == user:
    c = 1
else:
    while n != user:
        c = c + 1
        if n > user:
            print('Mais...tente mais uma vez.')
            user = int(input('Qual seu palpite? '))
        elif n < user:
            print('Menos... tente mais uma vez.')
            user = int(input('Qual seu palpite? '))
print('Acertou com {} tentativas, parabéns!!!'.format(c))
