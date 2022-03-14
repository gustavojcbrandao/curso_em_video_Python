from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        k = randint(1, 10)
        lista.append(k)
        print(f'{k} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista} temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
