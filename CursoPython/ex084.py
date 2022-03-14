pessoas = []
add = []
maior = menor = 0
while True:
    add.append(str(input('Nome: ')))
    add.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = add[1]
    else:
        if add[1] > maior:
            maior = add[1]
        if add[1] < menor:
            menor = add[1]
    pessoas.append(add[:])
    add.clear()
    teste = input('Deseja continuar? [S/N] ').strip().upper()
    if teste in 'N':
        break
print('=' * 30)
print(f'Foram cadastradas {len(pessoas)}')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end = '')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
