print('Gerador de PA')
print('-=-' * 7)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
c = primeiro
ultimo = primeiro + razao * 10
while c < ultimo:
    print('{} '.format(c), end='')
    if c < ultimo:
        print('-> ', end='')
    c = c + razao
print('FIM')