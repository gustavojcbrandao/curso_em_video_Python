distancia = float(input('Digite a distância total da viagem: '))
if distancia > 200:
    print('O Valor total de sua viagem é de: R${:.2f}'.format(distancia * 0.45))
else:
    print('O Valor total de sua viagem é de: R${:.2ff}'.format(distancia * 0.5))