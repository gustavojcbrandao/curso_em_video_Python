seg1 = int(input('Segmento 1: '))
seg2 = int(input('Segmento 2: '))
seg3 = int(input('Segmento 3: '))
if seg1 > seg2 + seg3 or seg2 > seg1 + seg3 or seg3 > seg1 + seg2:
    print('Não é possível construir um triângulo com estes segmentos')
elif seg1 == seg2 and seg2 == seg3:
    print('Estes segmentos formam um triângulo EQUILÁTERO')
elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
    print('Estes segmentos formam um triângulo ESCALENO')
else:
    print('Estes segmentos formam um triângulo ISOSCELES')
