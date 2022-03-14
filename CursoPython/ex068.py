from random import randint
cont = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
while True:
    n = int(input('Diga um valor: '))
    jogador = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    if jogador in 'PI':
        jogador = jogador
    else: jogador = str(input('Par ou ímpar? ')).upper()
    pcn = randint(0,10)
    if (n + pcn) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-' * 60)
    print(f'Você Jogou {n} e o computador jogou {pcn}. Total de {n + pcn} deu {resultado}')

    if resultado == jogador:
        print('-'*60)
        print('Você ganhou!!! Párabens!')
        print('Vamos jogar novamente...')
        print('=-' * 30)
    else:
        print('-' * 60)
        print('Você perdeu!!! Que pena!')
        break
    cont += 1
print('=-' * 30)
print(f'GAME OVER! Você venceu {cont} vezes.')
print('Obrigado por Jogar o Par ou Ímpar em Python')
