from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar emm um número entre 0 e 5. Tente adivinha...')
print('-=-'*20)
nu = int(input('Em qual número eu pensei? '))
nt = randint(1,5)
print('PROCESSANDO...')
sleep(1)
if nu == nt:
    print('Parabéns você conseguiu me vencer')
else:
    print('Você errou eu pensei em {} e você digitou {}'.format(nt, nu))
