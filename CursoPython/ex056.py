somaidade = int()
maisvelho = int()
homemmaisvelho = ''
qtdmulher = int()
for c in range(1, 5):
    print('----{}ª Pessoa-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaidade = somaidade + idade
    sexo = str(input('Sexo (M ou F): ')).upper()
    if sexo == 'M' and idade > maisvelho:
        homemmaisvelho = nome
        maisvelho = idade
    if sexo == 'F' and idade <= 20:
        qtdmulher = qtdmulher + 1
print('A média de idade do grupo é de {} anos.'.format(somaidade/4))
print('O homem mais velho é {} e ele tem {} anos.'.format(homemmaisvelho, maisvelho))
print('A quantidade de mulheres com menos de 20 anos é {}.'.format(qtdmulher))
