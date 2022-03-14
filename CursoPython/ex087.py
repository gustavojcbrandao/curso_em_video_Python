matriz = [[], [], []]
pares = terceira = segunda = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = (int(input(f'Digite um valor para [{l},{c}]: ')))
        matriz[l].append(n)
        if n % 2 == 0:
            pares = pares + n
        if c == 2:
            terceira = terceira + n
        if l == 1:
            if n > segunda:
                segunda = n
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {segunda}')
