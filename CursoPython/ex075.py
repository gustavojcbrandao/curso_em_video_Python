n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
lista = (n1, n2, n3, n4)
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O primeiro número 3 apareceu na posição {lista.index(3) + 1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
