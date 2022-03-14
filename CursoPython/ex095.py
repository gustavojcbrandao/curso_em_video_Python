time = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador["nome"] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogos):
        n = (int(input(f"Quantos gols na partida {c+1}: ")))
        total += n
        gols.append(n)
    jogador["gols"] = gols[:]
    jogador["total"] = total
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total = 0
    teste = str(input('Quer continuar? [S/N] ')).strip().upper()
    if teste in 'N':
        break
print('-=' * 30)
print(f'cod nome      gols      total')
print('-' * 30)
for i, v in enumerate(time):
    print(f'{i:<4}{v["nome"]:10}{v["gols"]:}{v["total"]:>5}')
print('-' * 30)
while True:
    consulta = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if consulta <= len(time) - 1:
        print(f' —— LEVANTAMENTO DO JOGADOR {time[consulta]["nome"]}:')
        for a, b in enumerate(time[consulta]["gols"]):
            print(f'  => Na partida {a+1}, fez {b} gols.')
        print('-' * 30)
    elif consulta == 999:
        break
    else:
        print(f'Erro! Não existe jogado com código {consulta}.')
