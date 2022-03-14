teste = 0
n = int(input('Digite o número que deseja testar se é primo: '))
for c in range(2, n):
    if n % c == 0:
        teste = teste + 1
if teste == 0:
    print('O número é primo')
else:
    print ('O número não é primo')
