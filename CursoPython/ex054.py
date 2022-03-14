from datetime import date
n = 0
for c in range(1,7):
    data = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    if data <= date.today().year - 21:
        n = n + 1
print('O total de pessoas maior de idade é {}'.format(n))
print('O total de pessoas que não atingiram a maior idade é de {}.'.format(6 - n))
