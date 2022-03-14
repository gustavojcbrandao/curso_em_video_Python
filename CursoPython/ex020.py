import random
a1 = input('Primeiro Aluno: ')
a2 = input('Segunndo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
#print('A ordem de apresentação será \n{}'.format(random.sample(lista,4)))
print('A ordem de apresentação será \n{}'.format(lista))
