frase = str(input('Digite uma frase: ')).strip()
frase = (frase.replace(" ",""))
inverso = frase[::-1]
#print(frase)
#print(inverso)
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
