def maior(* num):
    maior = c = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for k in num:
        print(f'{k}', end=' ')
        c += 1
        if c == 0:
            maior = k
        else:
            if k > maior:
                maior = k

    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
