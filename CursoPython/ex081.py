lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    teste = (input('Deseja continuar: [S/N] ')).strip().upper()
    if teste not in 'sS':
        break
print(f'Foram digitados {len(lista)} valores na lista')
lista.sort(reverse=True)
print(f'A lista de valores em forma decrescente é {lista}')
if 5 not in lista:
    print('O valor 5 não foi digitado')
else:
    print(f'O valor 5 foi digitado na posição', end=' ')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i}...', end=' ')
