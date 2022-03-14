c50 = c20 = c10 = c5 = c1 = 0
print('=' * 60)
print('{: ^60}'.format('BANCO CEV'))
print('=' * 60)
while True:
    saldo = int(input('Que valor você quer sacar? R$'))
    while saldo >= 50:
        saldo = saldo - 50
        c50 += 1
    if c50 > 0:
        print(f'Total de {c50} cédulas de R$50')
    while saldo >= 20:
        saldo = saldo - 20
        c20 += 1
    if c20 > 0:
        print(f'Total de {c20} cédulas de R$20')
    while saldo >= 10:
        saldo = saldo - 10
        c10 += 1
    if c10 > 0:
        print(f'Total de {c10} cédulas de R$10')
    while saldo >= 1:
        saldo = saldo - 1
        c1 += 1
    if c1 > 0:
        print(f'Total de {c1} cédulas de R$1')
    print('=' * 60)
    if saldo == 0:
        break
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
if saldo == 0:
    print(saldo)
elif saldo == 1:
    print(saldo + 1)
elif saldo == 2:
    print(saldo + 2)
else:
    print(saldo +3)
    

