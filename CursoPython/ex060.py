n = int(input('Digite um número para cálcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!  = '.format(n), end='')
while c > 0:
    f *= c
    print('{} '.format(c), end='')
    if c > 1:
        print('x ', end='')
    else: print('= ', end='')
    c -= 1
print('{}'.format(f))
