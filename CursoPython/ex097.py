def escreva(str):
    borda = len(str) + 4
    print('~' * borda)
    print(f'  {str}')
    print('~' * borda)


a = 'Gustavo Guanabara'
b = 'Curso de Python no YouTube'
c = 'CeV'

escreva(a)
escreva(b)
escreva(c)
