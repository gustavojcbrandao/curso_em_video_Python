total = cont = maisbarato = 0
nmaisbarato = ''
print('-' * 60)
print('{: ^60}'.format('LOJA SUPER BARATÃO'))
print('-' * 60)
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço R$'))
    total += preco
    if preco > 1000:
        cont += 1
    if maisbarato == 0 or preco < maisbarato:
        maisbarato = preco
        nmaisbarato = nome
    teste = ' '
    while teste not in 'SN':
        teste = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if teste == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi RS${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nmaisbarato} que custa R${maisbarato:.2f}')
