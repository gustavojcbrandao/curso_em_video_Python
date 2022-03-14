def leiaDinheiro(preço):
    while True:
        preço = str(input('Digite o preço: R$').replace(',', '.').strip())
        if preço.isalpha() is True or preço == '':
            print(f'\033[0;31m ERRO "{preço}" é um preço invalido\033[m')
        else:
            preço = float(preço)
            break
    return float(preço)
