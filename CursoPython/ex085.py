lista = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        lista[0].insert(0, n)
    else:
        lista[1].insert(1, n)
print('-=' * 30)
lista[0].sort()
print(f'A lista de números pares é {lista[0]}')
lista[1].sort()
print(f'A lista de números ímpares é {lista[1]}')
