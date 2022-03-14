print('Gerador de PA')
print('-=-' * 7)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
c = primeiro
t = ''
count = 0
ultimo = primeiro + razao * 10
while t != 0:
    while c < ultimo:
        print('{} '.format(c), end='')
        if c < ultimo:
            print('-> ', end='')
        c = c + razao
        count = count + 1
    print('PAUSA')
    t = int(input('Quantos termos a mais quer mostrar? '))
    ultimo = ultimo + razao * t
print('Progressão finalizada com {} termos mostrados'.format(count))
