sexo = str(input('Digite o seu sexo (M ou F): ')).strip
while sexo not in('mMfF'):
    sexo = input('Dados inválido. Por favor, informe o seu sexo: ').strip().uper()
print('Sexo {} registrado com sucesso.'.format(sexo))
