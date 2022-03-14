n = int(input('Informe o número que deseja testar: '))
resto = n % 2
if resto == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
print(resto)