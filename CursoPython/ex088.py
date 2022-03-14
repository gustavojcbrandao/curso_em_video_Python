from random import randint
from time import sleep
lista = []
print('-' * 30)
print('       JOGA NA MEGA SENA      ')
print('-' * 30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 5, f'SORTEANDO {qtd} JOGOS', '=-' * 5)
for c in range(0, qtd):
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        lista.sort()
    print(f'Jogo {c + 1}: {lista}')
    sleep(1)
    lista = []
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
