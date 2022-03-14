cadastro = dict()
mulheres = list()
pessoas = list()
maiorqmedia = list()
teste = ''
cont = media = sidade = 0
while True:
    cadastro["nome"] = (str(input('Nome: ')))
    while True:
        sexo = (str(input('Sexo [M/F]: '))).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Por favor digite apenas M ou F.')
        else:
            cadastro["sexo"] = sexo
            if cadastro["sexo"] == 'F':
                mulheres.append(cadastro["nome"])
            break
    cadastro["idade"] = (int(input('Idade: ')))
    sidade += cadastro["idade"]
    cont += 1
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while True:
        teste = (str(input('Quer continuar? [S/N]: '))).strip().upper()
        if teste in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if teste == 'N':
        break
media = sidade/cont
for c in pessoas:
    if c["idade"] > media:
        maiorqmedia.append(c['nome'])
print(f'A todo temos {len(pessoas)} cadastradas.')
print(f'A média das idades é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista das pessoas que estão acima da média: {maiorqmedia}')
