def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}m x {c:.1f}m é de {a:.1f}m².')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
