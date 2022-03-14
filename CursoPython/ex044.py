print('='*5, 'LOJAS BRANDÃO', '='*5)
preco = float(input('Informe o preço total das compras R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro ou cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
forma = int(input('Qual é a opção: '))
if forma == 1:
    print('Você ganhou um desconto de 10% sobre o preço de {}'.format(preco))
    print('O valor a ser pago é de R${:.2f}'.format(preco*0.9))
elif forma == 2:
    print('Você ganhou um desconto de 5% sobre o preço de {}'.format(preco))
    print('O valor a ser pago é de R${:.2f}'.format(preco*0.95))
elif forma == 3:
    print('O valor a ser pago é de R${:.2f} em 2x iguais de R${:.2f}'.format(preco, preco/2))
elif forma == 4:
    n = int(input('Quantas parcelas? '))
    print('Você vai pagar juros de 20% sobre o preço de {}'.format(preco))
    print('O valor a ser pago é de R${:.2f} em {}x iguais de R${:.2f}'.format(preco*1.2, n, (preco*1.2)/n))
else:
    print('Opção de pagamento inválida')
