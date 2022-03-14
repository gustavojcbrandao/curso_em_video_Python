n = count = soma = maior = menor = 0
teste = ''
while teste in 'sS':
    n = int(input('Digite um número: '))
    teste = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    count += 1
    soma += n
    if count == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('A média entre os {} valores digitados é igual a {:.2f}.'.format(count, soma/count))
