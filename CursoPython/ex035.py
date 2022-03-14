a = int(input('Digite o comprimento do primeiro segmento: '))
b = int(input('Digite o comprimento do segundo segmento: '))
c = int(input('Digite o comprimento do terceiro segmento: '))
ab = a + b
ac = a + c
bc = b + c
if a > bc or b > ac or c > ab:
    print('Os segmentos informados não podem formar um triângulo')
else:
    print('Os segmentos informados pode formar um triângulo')
