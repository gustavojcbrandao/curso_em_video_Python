count = 0
s = 0
for c in range(0,6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s = s + n
        count = count + 1
print('A soma dos {} valores pares informados é igual a {}'.format(count, s))
