t = int(input('Quantos dias alugados? '))
d = float(input('Quantos Km rodados? '))
vt = 60
vd = 0.15
total = (t*vt)+(d*vd)
print('O total a pagar é de R${:.2f}'.format(total))
