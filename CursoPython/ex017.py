import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#h = sqrt(pow(co, 2)+pow(ca, 2))
#h = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co,ca)))
