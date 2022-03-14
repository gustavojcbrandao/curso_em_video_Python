def leiaInt(msg):
    global n
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
