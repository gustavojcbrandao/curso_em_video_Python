from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
print('Valores sorteados:')
for a, b in jogo.items():
    print(f'{a} tirou {b} no dado.')
#    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for a, b in enumerate(ranking):
    print(f'{a+1}ª lugar {b[0]} com {b[1]}')
print(jogo)