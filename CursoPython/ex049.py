n = int(input('Digite o número que deseja calcular a tabuada: '))
print('='*20)
print('A tabuada de {} é:'.format(n))
for c in range(0,11):
    print('{:2} x {:2} = {:2}'.format(n, c, n*c))
print('='*20)