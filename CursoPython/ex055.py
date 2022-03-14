maior = int()
menor = int()
for c in range(1, 6):
    peso = float(input('Digite o peso da pessoa {} em quilogramas: '.format(c)))
    if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {:.1}kg e o menor peso foi {:.1}kg'.format(maior, menor))
