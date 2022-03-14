teste = 'S'
lista = []
while True:
    if teste == 'S':
        n = int(input('Digite um valor: '))
        if n not in lista:
            lista.append(n)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! Não vou adicionar...')
        teste = str(input('Deseja continuar? [S/N] ')).strip().upper()
    else:
        break
lista.sort()
print(f'Você digitou os valores {lista}')
