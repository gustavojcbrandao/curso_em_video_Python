n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2)/2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
if media < 5:
    print('O aluno está \033[0:31mREPROVADO\033[m')
if 5 <= media < 7:
    print('O aluno está \033[0:33mEM RECUPERAÇÃO\033[m')
if media >= 7:
    print('O aluno está \033[0:32mAPROVADO\033[m')
