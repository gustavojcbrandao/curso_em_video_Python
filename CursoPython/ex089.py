alunos = []
temp = []
cont = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    teste = str(input('Quer Continuar? [S/N] ')).strip().upper()
    alunos.append(temp[:])
    cont += 1
    temp.clear()
    if teste == 'N':
        break
print('-' * 25)
print('No. NOME            MÉDIA')
print('-' * 25)
for c in range(0,cont):
    print(f'{c:<3} {alunos[c][0]:<15} {(alunos[c][1]+alunos[c][2])/2:>5}')
print('-' * 25)
while True:
    search = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if search == 999:
        break
    else:
        print(f'Notas de {alunos[search][0]} são [{alunos[search][1]:.1f}, {alunos[search][2]:.1f}]')

print('Finalizando...')
print('<<<<Volte Sempre>>>>')
