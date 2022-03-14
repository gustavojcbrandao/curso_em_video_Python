teste = 's'
maior18 = totalhomem = mulhermenor20 = 0
while teste != 'N':
    print('-' * 60)
    print('CADASTRE UMA PESSOA')
    print('-' * 60)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
    print('-' * 60)
    if idade > 18:
        maior18 += 1
    if sexo == 'H':
        totalhomem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    teste = ' '
    while teste not in 'SN':
        teste = str(input('Quer continuar? [S/N] ')).upper()[0]
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao total temos {totalhomem} homens cadastrados')
print(f'E temos {mulhermenor20} mulheres com menos de 20 anos')
