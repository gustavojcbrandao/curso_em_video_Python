print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
contador = 0
anterior = 0
fibonacci = 0
termo = 1
if n == 1:
    print('0 → ', end='')
elif n == 2:
    print('0 → 1 →', end='')
else:
    print('0 → 1 → ', end='')
    while contador < n-2:
        contador = contador + 1
        fibonacci = anterior + termo
        print('{} → '.format(fibonacci), end='')
        anterior = termo
        termo = fibonacci
print('Fim')
