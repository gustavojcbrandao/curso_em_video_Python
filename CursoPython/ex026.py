n = str(input('Digite a frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(n.count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(n.find('a')+1))
print('A letra A aparece pela última vez na posição {}'.format(n.rfind('a')+1))


