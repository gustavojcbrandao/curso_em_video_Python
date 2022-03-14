termo1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da PA: '))
for c in range(termo1, termo1 + (razao * 10), razao):
    print(c, end='>')
print('Fim')
