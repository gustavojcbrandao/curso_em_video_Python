from time import sleep


def contador(a, b, c):
    print('-=' * 30)
    if c == 0 or a == b:
        print('Não é possível contar com passo = 0 ou valores de início e fim iguais')
    else:
        if a < b:
            c = abs(c)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            while a <= b:
                print(f'{a} ', end='')
                a += c
                sleep(0.5)
            print('FIM!')

        elif a > b:
            c = abs(c) * -1
            print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
            while a >= b:
                print(f'{a} ', end='')
                a += c
                sleep(0.5)
            print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)