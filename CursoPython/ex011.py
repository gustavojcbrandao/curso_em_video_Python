l = float(input('Digite o valor da largura da parede:'))
h = float(input('Informe o valor da altura da parede:'))
area = l * h
tinta = area/2
print('Sua parede tem a dimensão de {:.2f}x{:.2f}m e sua área é de {:.2f}m²'.format(l, h, area))
print('Para pintar essa parede, você vai precisar de {:.2f}l de tinta'.format(tinta))