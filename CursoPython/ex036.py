valor = float(input('Informe o valor do imóvel a ser finaciado R$'))
salário = float(input('Informe o salário do comprador do imóvel R$'))
prazo = int(input('Informe em quantos anos deseja realizar o financiamento: '))
prestação = valor / (prazo * 12)
limite = salário * 0.3
print('Para pagar um imóvel de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, prazo, prestação))
if prestação > limite:
    print('Infelizmente o financiamento não pode ser concedido pois o valor da parcela de R${:.2f} excede o limite de 30% do seu salário que é R${:.2f}'.format(prestação,limite))
else:
    print('O financiamento foi autorizado')