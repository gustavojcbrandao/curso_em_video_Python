escolha = ''
maior = ''
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
while escolha != 5:
    print('-' * 20)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair')
    print('-' * 20)
    escolha = int(input('>>> Qual é a sua opção? '))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é {}'.format(maior))
        else:
            print('Os números são iguais!!!')
    elif escolha == 4:
        print('Insira novos valores: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    else:
        print('Opção Inválida, faça uma nova escolha.')
print('Obrigado por usar nossos serviço.')