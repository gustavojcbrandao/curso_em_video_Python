salario = float(input('Digite o seu salário: R$'))
if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print('Seu salário com aumento agora é R${:.2f}'.format(salario))
