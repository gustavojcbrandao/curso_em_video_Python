frase = str(input('Digite a frase a ser testada: ')).strip().upper().replace(' ','')
inverso =''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]
if frase == inverso:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')
