jogador = dict()
gols = list()
total = 0
jogador["nome"] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, jogos):
    n = (int(input(f"Quantos gols na partida {c+1}: ")))
    total += n
    gols.append(n)
jogador["gols"] = gols
jogador["total"] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for i, v in enumerate(gols):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {total} gols')
