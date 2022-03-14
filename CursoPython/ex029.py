velocidade = float(input('Diggite a velocidade atual: '))
if velocidade > 80:
    print('Você foi multado! O valor da multa é de R${:.2}'.format((velocidade - 80) * 7))
print('Siga em frente e tenha uma boa viagem!')
