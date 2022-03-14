times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'America Mineiro', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A posição da Chapecoense é: {times.index("Chapecoense")}')
print('-=' * 15)
