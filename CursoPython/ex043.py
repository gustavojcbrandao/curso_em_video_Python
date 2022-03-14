peso = float(input('Informe o peso em quilogramas: '))
altura = float(input('Informe a altura em metros: '))
IMC = peso/altura**2
print('Seu IMC é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('IMC abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif IMC >= 40:
    print('Obesidade Mórbida')
