from random import randint

lista = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: {lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]}')
print(f'O maior valor sorteado foi {max(lista)}.')
print(f'O menor valor sorteado foi {min(lista)}.')
