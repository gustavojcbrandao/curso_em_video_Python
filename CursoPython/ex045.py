from random import randint
from time import sleep
print('Suas Opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
if jogador == 0:
    jogadajogador = 'PEDRA'
elif jogador == 1:
    jogadajogador = 'PAPEL'
elif jogador == 2:
    jogadajogador = 'TESOURA'
if computador == 0:
    jogadacomputador = 'PEDRA'
elif computador == 1:
    jogadacomputador = 'PAPEL'
elif computador == 2:
    jogadacomputador = 'TESOURA'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=-'*8)
print('Computador jogou {}'.format(jogadacomputador))
print('Jogador jogou {}'.format(jogadajogador))
print('-=-'*8)
if jogadacomputador == jogadajogador:
    print('O jogo foi empatado')
elif jogadacomputador == 'PEDRA' and jogadajogador == 'TESOURA':
    print('O Computador venceu')
elif jogadacomputador == 'PEDRA' and jogadajogador == 'PAPEL':
    print('O Jogador venceu')
elif jogadacomputador == 'PAPEL' and jogadajogador == 'TESOURA':
    print('O jogador venceu')
elif jogadacomputador == 'PAPEL' and jogadajogador == 'PEDRA':
    print('O computador venceu')
elif jogadacomputador == 'TESOURA' and jogadajogador == 'PEDRA':
    print('O Jogador venceu')
elif jogadacomputador == 'TESOURA' and jogadajogador == 'PAPEL':
    print('O Computador venceu')
