def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


#Programa Principal
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
