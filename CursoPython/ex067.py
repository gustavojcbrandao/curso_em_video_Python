while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n > 0:
        for c in range(1,11):
            print(f'{n} x {c:2} = {n * c}')
        print('-' * 30)
    else:
        break
print('PROGRAMA DE TABUADA ENCERRADO. Volte Sempre!')
