c = 0
lista = str(input('Digite a expressão: '))
while True:
    for i, v in enumerate(lista):
        if v == '(':
            c += 1
        elif v == ')':
            c += -1
        if c < 0:
            break
    break
if c == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')
